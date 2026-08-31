from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import ResearchPublication, Story, Milestone, TeamMember


@override_settings(SECURE_SSL_REDIRECT=False)
class PageSmokeTests(TestCase):
    def test_home_returns_200_with_content(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'High Tech Pioneer')
        self.assertContains(response, 'taught')

    def test_about_lists_milestones_and_team(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Muni Bahadur Sakya')
        self.assertContains(response, 'ICT Pioneer Award')

    def test_research_lists_publications(self):
        response = self.client.get(reverse('research'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Segment Anything but Farms')

    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dillibazar')

    def test_robots_txt(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sitemap:')

    def test_sitemap_xml(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<urlset')

    def test_404_page_is_custom(self):
        response = self.client.get('/this/page/does/not/exist/')
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'That page', status_code=404)


@override_settings(SECURE_SSL_REDIRECT=False)
class VideoEndpointTests(TestCase):
    def test_range_request_streams_partial_content(self):
        response = self.client.get(
            reverse('stream_video', args=['building_base_robot.mp4']),
            HTTP_RANGE='bytes=0-1023',
        )
        self.assertEqual(response.status_code, 206)
        self.assertEqual(response['Accept-Ranges'], 'bytes')
        self.assertTrue(response['Content-Range'].startswith('bytes 0-1023/'))

    def test_full_request_streams_200(self):
        response = self.client.get(reverse('stream_video', args=['building_base_robot.mp4']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Accept-Ranges'], 'bytes')

    def test_path_traversal_is_rejected(self):
        for bad in ['..%2F..%2Fetc%2Fpasswd.mov', 'secret.txt', '../../manage.py']:
            response = self.client.get(f'/video/{bad}')
            self.assertIn(response.status_code, (404, 400))

    def test_missing_video_is_404(self):
        response = self.client.get(reverse('stream_video', args=['no_such_file.mp4']))
        self.assertEqual(response.status_code, 404)


@override_settings(SECURE_SSL_REDIRECT=False)
class SeedDataTests(TestCase):
    def test_verified_seed_present(self):
        self.assertGreaterEqual(Milestone.objects.count(), 15)
        self.assertGreaterEqual(TeamMember.objects.count(), 4)
        self.assertTrue(
            ResearchPublication.objects.filter(
                title__startswith='Segment Anything but Farms'
            ).exists()
        )
        self.assertGreaterEqual(Story.objects.count(), 5)

    def test_story_media_files_exist(self):
        for story in Story.objects.all():
            if story.media_url.startswith('/static/'):
                path = settings.BASE_DIR / story.media_url.lstrip('/')
                self.assertTrue(path.exists(), f'missing: {story.media_url}')

    def test_milestone_ordering_is_chronological_years(self):
        years = [m.year for m in Milestone.objects.all()]
        self.assertEqual(years[0], '1962')
        self.assertIn('17 May 2006', years)

    def test_team_founder_is_first(self):
        first = TeamMember.objects.first()
        self.assertEqual(first.role_type, 'founder')
