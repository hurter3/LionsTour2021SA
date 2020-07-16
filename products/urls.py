from django.conf.urls import url, include
from .views import ProductListView, ProductDetailView, ProductListAll

urlpatterns = [
 url(r'^$', ProductListAll.as_view(), name='product-list-all'),
 url(r'(?P<pk>\d+)/', ProductDetailView.as_view(), name='product-detail'),
 url(r'(?P<category>[\w\-]+)/', ProductListView.as_view(), name='product-list-view'),
]