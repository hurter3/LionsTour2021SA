from django.conf.urls import url, include
#from .views import all_products, ProductListView
from .views import ProductListView, ProductDetailView, ProductListMenView

urlpatterns = [
# url(r'^$', all_products, name='products'),
 url(r'^$', ProductListView.as_view(), name='product-list-all'),
 url(r'^$', ProductListMenView.as_view(), name='product-list-men'),
# url(r'^product/(?P<category>)/$', ProductListView.as_view(), name='product-list'),
 url(r'(?P<pk>\d+)/', ProductDetailView.as_view(), name='product-detail'),
]