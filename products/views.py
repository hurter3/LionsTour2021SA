from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView, ListView

#class ProductListView(ListView):
#    paginate_by = 4
#    queryset = Product.objects.all()
#    model = Product
#    template_name = 'products.html'
#    context_object_name = 'products'


#class ProductListMenView(ListView):
#    paginate_by = 4
#    queryset = Product.objects.all().filter(category="Men")
#    model = Product
#    template_name = 'products.html'
#    context_object_name = 'products'

#class ProductListWomanView(ListView):
#    paginate_by = 4
#    queryset = Product.objects.all().filter(category="Woman")
#    model = Product
#    template_name = 'products.html'
#    context_object_name = 'products'

#class ProductListChildrenView(ListView):
#    paginate_by = 4
#    queryset = Product.objects.all().filter(category="Children")
#    model = Product
#    template_name = 'products.html'
#    context_object_name = 'products'

#class ProductListSouvenirsView(ListView):
#    paginate_by = 4
#    queryset = Product.objects.all().filter(category="Souvenirs")
#    model = Product
#    template_name = 'products.html'
#    context_object_name = 'products'
    
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'products'


class ProductListView(ListView):
    paginate_by = 4
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        if self.kwargs['category'] == 'All':
            return Product.objects.all()
        else:
            return Product.objects.filter(category=self.kwargs['category'])

