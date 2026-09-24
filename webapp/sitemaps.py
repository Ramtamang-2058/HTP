from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    protocol = 'https'

    PRIORITIES = {
        'home': 1.0,
        'kancha': 0.9,
        'about': 0.8,
        'research': 0.7,
        'contact': 0.6,
    }

    def items(self):
        return list(self.PRIORITIES)

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return self.PRIORITIES[item]


sitemaps = {
    'static': StaticViewSitemap,
}
