from django.conf.urls import url, include
from .views import home_view, history_view, photos_view, tickets_view


urlpatterns = [
    url(r'^$', home_view, name='index'),
    url('history/', history_view, name="history"),
 ]