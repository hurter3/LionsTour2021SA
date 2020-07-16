from django.test import Client, TestCase

        
class TestCompetitionRulesView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/competition/rules/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/competition/rules/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('competition_rules.html', str(names))
        
class TestCompetitionTermsView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/competition/terms/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/competition/terms/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('competition_terms.html', str(names))
        
   
class TestCompetitionNewView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/competition/new')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/competition/new')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('competition.html', str(names))

# Helper functions
def get_names(templates):
    names = []
    for t in templates:
        names.append(t.name)
    return names