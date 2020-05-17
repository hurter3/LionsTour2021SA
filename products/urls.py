from django.conf.urls import url, include
#from .views import all_products, ProductListView
from .views import ProductListView

urlpatterns = [
# url(r'^$', all_products, name='products'),
 url(r'^$', ProductListView.as_view(), name='product-list'),
]