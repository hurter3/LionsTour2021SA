from django.conf.urls import url, include
from .views import score_prediction

urlpatterns = [
    url(r'^$', score_prediction, name='competition'),
]