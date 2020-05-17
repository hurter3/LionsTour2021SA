from django.shortcuts import render
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

