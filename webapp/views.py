import os
import re

from django.conf import settings
from django.http import HttpResponse, StreamingHttpResponse, Http404
from django.shortcuts import render

from .models import ResearchPublication, Story, Milestone, TeamMember


def _active_stories():
    return list(Story.objects.filter(is_active=True))


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


def robots(request):
    lines = ['User-agent: *', 'Disallow: /admin/', '', f'Sitemap: https://hightechpioneer.com.np/sitemap.xml']
    return HttpResponse('\n'.join(lines), content_type='text/plain')


def handler404(request, exception=None):
    return render(request, '404.html', status=404)


CONTENT_TYPES = {
    '.mov': 'video/quicktime',
    '.mp4': 'video/mp4',
    '.webm': 'video/webm',
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
