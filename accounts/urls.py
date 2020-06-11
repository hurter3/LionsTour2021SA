from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from .views import register_view, profile_view, order_detail_view

urlpatterns = [
    url('register/', register_view, name="register"),
    url('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name="login"),
    url('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    url('profile/', profile_view, name="profile"),
    url(r'^order-detail/(?P<id>\d+)', order_detail_view, name='order-detail'),
]

