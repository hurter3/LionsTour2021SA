from django.conf.urls import url, include
from .views import home_view, history_view, photos_view, fixtures_view, tickets_view, contact_view


urlpatterns = [
    url(r'^$', home_view, name='home'),
    url('history/', history_view, name="history"),
    url('photos/', photos_view, name="photos"),
    url('fixtures/', fixtures_view, name="fixtures"),
    url('tickets/', tickets_view, name="tickets"),
    url('contact/', contact_view, name="contact"),
]
