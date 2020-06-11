from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from checkout.models import Order, OrderLineItem

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile_view(request):
    orders = Order.objects.filter(customer=request.user)
    print(orders)
    return render(request, 'profile.html', {'orders': orders})


def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


#def order_details(request, order_id, template_name="registration/order_details.html"):
## order = get_object_or_404(Order, id=order_id, user=request.user)
 #page_title = 'Order Details for Order #' + order_id
 #order_items = OrderItem.objects.filter(order=order)
 #return render_to_response(template_name, locals(),
 #context_instance=RequestContext(request)) 

