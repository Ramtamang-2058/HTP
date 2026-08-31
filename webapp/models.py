from django.db import models


class ResearchPublication(models.Model):
    CATEGORY_CHOICES = [
        ('robotics', 'Robotics'),
        ('ai', 'Artificial Intelligence'),
        ('nlp', 'NLP & Devanagari'),
        ('connectivity', 'Connectivity'),
        ('hpc', 'High Performance Computing'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=500, help_text="Comma-separated author names")
    venue = models.CharField(max_length=200, blank=True, help_text="Journal, conference, or 'Preprint'")
    abstract = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags")
    pdf_file = models.FileField(upload_to='research/pdfs/', blank=True, null=True)
    github_url = models.URLField(blank=True, help_text="Link to GitHub repository")
    external_url = models.URLField(blank=True, help_text="External paper link (arXiv, DOI, etc.)")
    published_date = models.DateField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'Research Publication'
        verbose_name_plural = 'Research Publications'

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    def get_authors_list(self):
        return [a.strip() for a in self.authors.split(',') if a.strip()]


class ProductMedia(models.Model):
    """A user-managed media slot shown on the shared product page.

    The shareable link stays constant — the file, caption and order are swapped
    from the PIN-protected control panel without touching code.
    """
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    slot = models.CharField(max_length=50, unique=True, help_text="Stable key, e.g. 'video' or 'image_1'. Never changes after creation.")
    label = models.CharField(max_length=120, blank=True, help_text="Short label shown to viewers")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='product_media/', blank=True, null=True)
    fallback_path = models.CharField(max_length=500, blank=True, help_text="Optional static/media path used if no uploaded file is set, e.g. /static/img/robots/x.jpeg or /video/f.mp4")
    caption = models.CharField(max_length=300, blank=True)
    sort_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'slot']
        verbose_name = 'Product Media Slot'
        verbose_name_plural = 'Product Media Slots'

    def __str__(self):
        return f'{self.slot} — {self.label or self.media_type}'

    def effective_url(self):
        """Prefer the uploaded file, else fall back to a static path."""
        if self.file:
            return self.file.url
        return self.fallback_path or ''


class Story(models.Model):
    title = models.CharField(max_length=100)
    media_url = models.CharField(max_length=500, help_text="Path to static file (e.g., static/img/robots/robot_after_3d_print.jpeg) or full URL")
    thumbnail_url = models.CharField(max_length=500, blank=True, help_text="Optional path to static thumbnail. Defaults to media_url if empty.")
    caption = models.TextField(blank=True, help_text="Optional text caption to show on the story")
    media_type = models.CharField(max_length=20, choices=[('image', 'Image'), ('video', 'Video')], default='image')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        return self.thumbnail_url if self.thumbnail_url else self.media_url


class Milestone(models.Model):
    year = models.CharField(max_length=20, help_text="Year label, e.g. '1983' or '2004–05'")
    exact_date = models.DateField(blank=True, null=True, help_text="Optional exact date for sorting")
    sort_order = models.IntegerField(default=0, help_text="Ascending; used before year when equal")
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.CharField(max_length=500, blank=True, help_text="Path to static image (optional)")
    image_caption = models.CharField(max_length=300, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order']
        verbose_name = 'Milestone'
        verbose_name_plural = 'History Milestones'

    def __str__(self):
        return f'{self.year} — {self.title}'


class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('founder', 'Founder'),
        ('engineer', 'Engineer'),
        ('researcher', 'Researcher'),
        ('staff', 'Staff'),
    ]

    name = models.CharField(max_length=150)
    role = models.CharField(max_length=100)
    role_type = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')
    bio = models.TextField()
    photo = models.CharField(max_length=500, help_text="Path to static profile image")
    portfolio_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    scholar_url = models.URLField(blank=True)
    sort_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['sort_order']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.name
