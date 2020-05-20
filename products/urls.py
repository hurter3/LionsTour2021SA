from django.conf.urls import url, include
#from .views import all_products, ProductListView
from .views import ProductListView, ProductDetailView, ProductListMenView, ProductListWomanView,ProductListChildrenView, ProductListSouvenirsView

urlpatterns = [
# url(r'^$', all_products, name='products'),
 url(r'^$', ProductListView.as_view(), name='product-list-all'),
 url(r'product/men', ProductListMenView.as_view(), name='product-list-men'),
 url(r'product/woman', ProductListWomanView.as_view(), name='product-list-woman'),
 url(r'product/children', ProductListChildrenView.as_view(), name='product-list-children'),
 url(r'product/souvenirs', ProductListSouvenirsView.as_view(), name='product-list-souvenirs'),

 url(r'(?P<pk>\d+)/', ProductDetailView.as_view(), name='product-detail'),

# url(r'(?P<category>[\w\-]+)/', ProductListView.as_view(), name='product-list-view'),
# for navbat li link <a class="dropdown-item" href="{% url 'product-list-view' category='Men' %}">Men's</a>
]