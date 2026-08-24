from django.contrib import admin
from .models import ResearchPublication, Story, Milestone, TeamMember


@admin.register(ResearchPublication)
class ResearchPublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'venue', 'published_date', 'is_published')
    list_filter = ('category', 'is_published', 'published_date')
    search_fields = ('title', 'authors', 'abstract', 'venue')
    list_editable = ('is_published',)
    date_hierarchy = 'published_date'
    fieldsets = (
        ('Publication Info', {
            'fields': ('title', 'authors', 'venue', 'abstract', 'category', 'tags', 'published_date')
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


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'sort_order', 'is_active')
    list_editable = ('sort_order', 'is_active')
    search_fields = ('year', 'title', 'body')
    fieldsets = (
        (None, {'fields': ('year', 'exact_date', 'sort_order', 'title', 'body')}),
        ('Image', {'fields': ('image', 'image_caption')}),
        ('Visibility', {'fields': ('is_active',)}),
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'role_type', 'sort_order', 'is_active')
    list_editable = ('sort_order', 'is_active')
    search_fields = ('name', 'role', 'bio')
