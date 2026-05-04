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
    abstract = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags")
    pdf_file = models.FileField(upload_to='research/pdfs/', blank=True, null=True)
    github_url = models.URLField(blank=True, help_text="Link to GitHub repository")
    external_url = models.URLField(blank=True, help_text="External paper link (arXiv, etc.)")
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
