from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from accounts.views import register_view, profile_view, order_detail_view, change_email_view, confirm_delete_view

class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_view)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile_view)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)

    def test_change_email_url_is_resolved(self):
        url = reverse('change-email')
        self.assertEqual(resolve(url).func, change_email_view)
        
    def test_confirm_delete_url_is_resolved(self):
        url = reverse('confirm-delete')
        self.assertEqual(resolve(url).func, confirm_delete_view)