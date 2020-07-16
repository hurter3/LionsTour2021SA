from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User
from accounts.views import register_view, profile_view

class TestRegisterViewLoggedOut(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/accounts/register/')
        templates = response.templates
        names = get_names(templates)

        self.assertIn('base.html', str(names))
        self.assertIn('register.html', str(names))
       
class TestRegisterViewLoggedIn(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testinguser', email='testing@gmail.com', password="testing123"
        )
    

# Helper functions
def get_names(templates):
    names = []
    for t in templates:
        names.append(t.name)
    return names