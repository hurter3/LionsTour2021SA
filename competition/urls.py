from django.conf.urls import url, include
from .views import score_prediction, score_prediction_new, competition_rules_view, competition_terms_view

urlpatterns = [
    url(r'^update$', score_prediction, name='competition'),
    url(r'^new$', score_prediction_new, name='competition_new'),
    url(r'^rules/', competition_rules_view, name="competition-rules"),
    url(r'^terms/', competition_terms_view, name="competition-terms"),
]