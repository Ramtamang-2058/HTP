from django.contrib import admin
from .models import ResearchPublication, Story


@admin.register(ResearchPublication)
class ResearchPublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'authors', 'published_date', 'is_published')
    list_filter = ('category', 'is_published', 'published_date')
    search_fields = ('title', 'authors', 'abstract')
    list_editable = ('is_published',)
    date_hierarchy = 'published_date'
    fieldsets = (
        ('Publication Info', {
            'fields': ('title', 'authors', 'abstract', 'category', 'tags', 'published_date')
        }),
        ('Files & Links', {
            'fields': ('pdf_file', 'github_url', 'external_url')
        }),
        ('Visibility', {
            'fields': ('is_published',)
        }),
    )


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'order', 'is_active', 'created_at')
    list_filter = ('media_type', 'is_active')
    search_fields = ('title', 'caption')
    list_editable = ('order', 'is_active')

