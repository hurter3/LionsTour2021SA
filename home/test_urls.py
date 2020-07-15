from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home_view, history_view, fixtures_view, tickets_view, contact_view

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home_view)

    def test_history_url_is_resolved(self):
        url = reverse('history')
        self.assertEqual(resolve(url).func, history_view)

    def test_fixtures_url_is_resolved(self):
        url = reverse('fixtures')
        self.assertEqual(resolve(url).func, fixtures_view)

    def test_tickets_url_is_resolved(self):
        url = reverse('tickets')
        self.assertEqual(resolve(url).func, tickets_view)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact_view)
        