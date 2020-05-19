from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import DetailView, ListView

# Create your views here.
#def all_products(request):
#    products = Product.objects.all()
#    return render(request, "products.html", {"products": products})

class ProductListView(ListView):
   queryset = Product.objects.all()
   model = Product
   template_name = 'products.html'
   context_object_name = 'products'


class ProductListMenView(ListView):
   queryset = Product.objects.all().filter(category="Men")
   model = Product
   template_name = 'products.html'
   context_object_name = 'products'

class ProductListWomanView(ListView):
   queryset = Product.objects.all().filter(category="Woman")
   model = Product
   template_name = 'products.html'
   context_object_name = 'products'

class ProductListChildrenView(ListView):
   queryset = Product.objects.all().filter(category="Children")
   model = Product
   template_name = 'products.html'
   context_object_name = 'products'

class ProductListSouvenirsView(ListView):
   queryset = Product.objects.all().filter(category="Souvenirs")
   model = Product
   template_name = 'products.html'
   context_object_name = 'products'
   
#class ProductListView(ListView):
#    template_name = 'products.html'
#    context_object_name = 'products'
#    def get_queryset(self):
#        if self.kwargs['category']:
#            queryset = Product.objects.all()
#        else:
#            category_id = self.kwargs['category']
#            queryset = Product.objects.all().filter(category=category_id)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'products'