import os
import re
from django.shortcuts import render
from django.http import StreamingHttpResponse, Http404
from django.conf import settings
from .models import ResearchPublication, Story


def index(request):
    research = ResearchPublication.objects.filter(is_published=True)
    
    stories = []
    try:
        stories = list(Story.objects.filter(is_active=True))
    except Exception:
        pass

    if not stories:
        stories = [
            {
                'id': 1,
                'title': 'Muni Sakya',
                'get_thumbnail': '/static/img/profiles/muni_bahadur_sakya.png',
                'media_url': '/static/img/profiles/muni_bahadur_sakya.png',
                'media_type': 'image',
                'caption': "Founder Muni Bahadur Sakya demonstrating Nepal's first Devanagari computing (1983)."
            },
            {
                'id': 2,
                'title': '3D Robot Print',
                'get_thumbnail': '/static/img/robots/robot_after_3d_print.jpeg',
                'media_url': '/static/img/robots/robot_after_3d_print.jpeg',
                'media_type': 'image',
                'caption': 'InMoov humanoid robot frame assembled after 3D printing in the HTP lab.'
            },
            {
                'id': 3,
                'title': 'Hand Assembly',
                'get_thumbnail': '/static/img/robots/robots_hand_assembling.png',
                'media_url': '/static/img/robots/robots_hand_assembling.png',
                'media_type': 'image',
                'caption': 'Calibrating and assembling the mechanical hand degrees of freedom.'
            },
            {
                'id': 4,
                'title': 'Base Assembly',
                'get_thumbnail': '/static/img/robots/assembling_after_print_upper_body.jpeg',
                'media_url': '/video/building_base_robot.mov',
                'media_type': 'video',
                'caption': 'Video: Assembly of the mobile base robot in Dillibazar.'
            },
            {
                'id': 5,
                'title': 'Handshake Demo',
                'get_thumbnail': '/static/img/robots/left_hand_break.png',
                'media_url': '/video/handshke_robot.mov',
                'media_type': 'video',
                'caption': 'Video: Live humanoid robot handshake demonstration.'
            }
        ]
        
    return render(request, 'index.html', {'research': research, 'stories': stories})


def stream_video(request, filename):
    """
    Streams a video file from the static/videos/ directory with full
    HTTP byte-range (Range header) support so browsers can seek, pause,
    and resume large .mov / .mp4 files correctly.
    """
    # Security: only allow safe filenames (no path traversal)
    if not re.match(r'^[\w\-]+\.(mov|mp4|webm)$', filename):
        raise Http404("Invalid video filename")

    video_path = os.path.join(settings.BASE_DIR, 'static', 'videos', filename)
    if not os.path.exists(video_path):
        raise Http404("Video not found")

    file_size = os.path.getsize(video_path)
    content_type = 'video/mp4'

    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)

    CHUNK = 8 * 1024 * 1024  # 8 MB chunks

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
