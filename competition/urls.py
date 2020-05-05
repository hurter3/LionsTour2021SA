from django.conf.urls import url, include
from .views import prediction_scores

urlpatterns = [
    url(r'^$', prediction_scores, name='competition'),
]