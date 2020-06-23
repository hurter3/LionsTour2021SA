from django.conf.urls import url, include
#from .views import all_products, ProductListView
from .views import ProductListView, ProductDetailView, ProductListAll

urlpatterns = [
# url(r'^$', all_products, name='products'),
# url(r'^$', ProductListView.as_view(), name='product-list-all'),
 url(r'^$', ProductListAll.as_view(), name='product-list-all'),
# url(r'men/', ProductListView.as_view(), name='product-list-view'),
#  url(r'men/', ProductListMenView.as_view(), name='product-list-men'),
# url(r'woman/', ProductListWomanView.as_view(), name='product-list-woman'),
# url(r'children/', ProductListChildrenView.as_view(), name='product-list-children'),
# url(r'souvenirs/', ProductListSouvenirsView.as_view(), name='product-list-souvenirs'),

 url(r'(?P<pk>\d+)/', ProductDetailView.as_view(), name='product-detail'),

 url(r'(?P<category>[\w\-]+)/', ProductListView.as_view(), name='product-list-view'),
# for navbat li link <a class="dropdown-item" href="{% url 'product-list-view' category='Men' %}">Men's</a>
]