from django.test import SimpleTestCase
from django.urls import reverse, resolve
from competition.views import competition, competition_new, competition_rules_view, competition_terms_view

class TestUrls(SimpleTestCase):

    def test_competition_url_is_resolved(self):
        url = reverse('competition')
        self.assertEqual(resolve(url).func, competition)

    def test_competition_new_url_is_resolved(self):
        url = reverse('competition-new')
        self.assertEqual(resolve(url).func, competition_new)

    def test_compeition_rules_url_is_resolved(self):
        url = reverse('competition-rules')
        self.assertEqual(resolve(url).func, competition_rules_view)

    def test_competition_terms_url_is_resolved(self):
        url = reverse('competition-terms')
        self.assertEqual(resolve(url).func, competition_terms_view)

