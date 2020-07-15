from django.conf.urls import url, include
from .views import competition, competition_new, competition_rules_view, competition_terms_view

urlpatterns = [
    url(r'^update$', competition, name='competition'),
    url(r'^new$', competition_new, name='competition-new'),
    url(r'^rules/', competition_rules_view, name="competition-rules"),
    url(r'^terms/', competition_terms_view, name="competition-terms"),
]