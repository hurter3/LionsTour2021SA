from django.conf.urls import url, include
from .views import home_view

urlpatterns = [
    url(r'^$', home_view, name='index'),
]