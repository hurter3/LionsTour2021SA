from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView, ListView

class ProductListAll(ListView):
    paginate_by = 8
    queryset = list(Product.objects.all())
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'products'

class ProductListView(ListView):
    paginate_by = 8
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        if self.kwargs['category'] == 'All':
            return list(Product.objects.all())
        else:
            return list(Product.objects.filter(category=self.kwargs['category']))

