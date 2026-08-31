import os
import re

from django.conf import settings
from django.http import HttpResponse, StreamingHttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import ResearchPublication, Story, Milestone, TeamMember, ProductMedia


MEDIA_PIN = '2058'


def _active_stories():
    return list(Story.objects.filter(is_active=True))


def _active_media():
    return list(ProductMedia.objects.filter(is_active=True))


def home(request):
    context = {
        'stories': _active_stories(),
        'latest_research': ResearchPublication.objects.filter(is_published=True)[:2],
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'milestones': Milestone.objects.filter(is_active=True),
        'team': TeamMember.objects.filter(is_active=True),
    }
    return render(request, 'about.html', context)


def research(request):
    context = {
        'publications': ResearchPublication.objects.filter(is_published=True),
    }
    return render(request, 'research.html', context)


def contact(request):
    return render(request, 'contact.html')


def kancha(request):
    context = {
        'stories': _active_stories(),
        'media': _active_media(),
    }
    return render(request, 'kancha.html', context)


def robots(request):
    lines = ['User-agent: *', 'Disallow: /admin/', '', f'Sitemap: https://hightechpioneer.com.np/sitemap.xml']
    return HttpResponse('\n'.join(lines), content_type='text/plain')


def handler404(request, exception=None):
    return render(request, '404.html', status=404)


CONTENT_TYPES = {
    '.mov': 'video/quicktime',
    '.mp4': 'video/mp4',
    '.webm': 'video/webm',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.gif': 'image/gif',
    '.webp': 'image/webp',
}


def stream_video(request, filename):
    """
    Streams a video file from the static/videos/ directory with full
    HTTP byte-range support so browsers can seek, pause and resume.
    """
    if not re.match(r'^[\w\-]+\.(mov|mp4|webm)$', filename):
        raise Http404('Invalid video filename')

    video_path = os.path.join(settings.BASE_DIR, 'static', 'videos', filename)
    if not os.path.exists(video_path):
        raise Http404('Video not found')

    file_size = os.path.getsize(video_path)
    extension = os.path.splitext(filename)[1].lower()
    content_type = CONTENT_TYPES.get(extension, 'application/octet-stream')

    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)

    CHUNK = 8 * 1024 * 1024  # 8 MB

    if range_match:
        first_byte = int(range_match.group(1))
        last_byte = int(range_match.group(2)) if range_match.group(2) else min(first_byte + CHUNK - 1, file_size - 1)
        length = last_byte - first_byte + 1

        def file_iterator(path, offset, length, chunk=65536):
            with open(path, 'rb') as f:
                f.seek(offset)
                remaining = length
                while remaining > 0:
                    data = f.read(min(chunk, remaining))
                    if not data:
                        break
                    remaining -= len(data)
                    yield data

        response = StreamingHttpResponse(
            file_iterator(video_path, first_byte, length),
            status=206,
            content_type=content_type,
        )
        response['Content-Range'] = f'bytes {first_byte}-{last_byte}/{file_size}'
        response['Content-Length'] = str(length)
    else:
        def full_iterator(path, chunk=65536):
            with open(path, 'rb') as f:
                while True:
                    data = f.read(chunk)
                    if not data:
                        break
                    yield data

        response = StreamingHttpResponse(
            full_iterator(video_path),
            status=200,
            content_type=content_type,
        )
        response['Content-Length'] = str(file_size)

    response['Accept-Ranges'] = 'bytes'
    response['Cache-Control'] = 'public, max-age=3600'
    return response


def serve_media(request, slot):
    """Serve an uploaded ProductMedia file with byte-range support (video seeking)."""
    try:
        obj = ProductMedia.objects.get(slot=slot, is_active=True)
    except (ProductMedia.DoesNotExist, ValueError):
        raise Http404('No media for this slot')

    if not obj.file:
        raise Http404('No uploaded file for this slot')

    path = obj.file.path
    if not os.path.exists(path):
        raise Http404('Media file missing')

    ext = os.path.splitext(path)[1].lower()
    content_type = CONTENT_TYPES.get(ext, 'application/octet-stream')
    file_size = os.path.getsize(path)

    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)
    CHUNK = 8 * 1024 * 1024

    def file_iterator(p, offset, length, chunk=65536):
        with open(p, 'rb') as f:
            f.seek(offset)
            remaining = length
            while remaining > 0:
                data = f.read(min(chunk, remaining))
                if not data:
                    break
                remaining -= len(data)
                yield data

    if range_match:
        first_byte = int(range_match.group(1))
        last_byte = int(range_match.group(2)) if range_match.group(2) else min(first_byte + CHUNK - 1, file_size - 1)
        length = last_byte - first_byte + 1
        response = StreamingHttpResponse(
            file_iterator(path, first_byte, length),
            status=206, content_type=content_type,
        )
        response['Content-Range'] = f'bytes {first_byte}-{last_byte}/{file_size}'
        response['Content-Length'] = str(length)
    else:
        response = StreamingHttpResponse(
            file_iterator(path, 0, file_size),
            status=200, content_type=content_type,
        )
        response['Content-Length'] = str(file_size)

    response['Accept-Ranges'] = 'bytes'
    response['Cache-Control'] = 'public, max-age=3600'
    return response


def share_media(request):
    """Standalone, chrome-free page — this is the link people are sent."""
    media = _active_media()
    video = [m for m in media if m.media_type == 'video']
    images = [m for m in media if m.media_type == 'image']
    return render(request, 'share_media.html', {
        'video': video[0] if video else None,
        'images': images,
    })


def media_manager(request):
    """PIN-protected control panel to swap media without touching code."""
    authed = request.session.get('media_authed', False)

    if request.method == 'POST':
        action = request.POST.get('action')
        if not authed:
            if request.POST.get('pin') == MEDIA_PIN:
                request.session['media_authed'] = True
                authed = True
            else:
                return render(request, 'media_manager.html', {
                    'authed': False, 'error': 'Incorrect PIN.',
                })

        if authed:
            slot = request.POST.get('slot')
            if action == 'update' and slot:
                try:
                    obj = ProductMedia.objects.get(slot=slot)
                except ProductMedia.DoesNotExist:
                    obj = None
                if obj:
                    new_file = request.FILES.get('file')
                    if new_file:
                        obj.file = new_file
                    caption = request.POST.get('caption')
                    if caption is not None:
                        obj.caption = caption.strip()
                    active = request.POST.get('is_active')
                    obj.is_active = (active == 'on')
                    obj.save()
            elif action == 'logout':
                del request.session['media_authed']
                authed = False
        return redirect('media_manager')

    slots = ProductMedia.objects.all()
    return render(request, 'media_manager.html', {
        'authed': authed,
        'slots': slots,
    })
