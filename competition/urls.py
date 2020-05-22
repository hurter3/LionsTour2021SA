from django.conf.urls import url, include
from .views import score_prediction, score_prediction_new

urlpatterns = [
    url(r'^update$', score_prediction, name='competition'),
    url(r'^new$', score_prediction_new, name='competition_new'),
]