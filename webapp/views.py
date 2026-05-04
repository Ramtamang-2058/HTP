from django.shortcuts import render
from .models import ResearchPublication


def index(request):
    research = ResearchPublication.objects.filter(is_published=True)
    return render(request, 'index.html', {'research': research})
