from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem, Order
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe
import datetime

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)

            cart = request.session.get('cart', {})
            total_qty = 0
            total_cost = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total_cost += quantity * product.price
                total_qty += quantity 

            order.customer = request.user
            order.date_ordered = datetime.datetime.now()
            order.total_quantity = total_qty
            order.total_cost = total_cost
            order.save()
           
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount= int(total_cost *100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.success(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        any_orders = Order.objects.filter(customer=request.user)
        if any_orders:
            last_order = Order.objects.filter(customer=request.user).order_by('-id')[0]
            order_form = OrderForm(instance=last_order)
            payment_form = MakePaymentForm()
        else:
            payment_form = MakePaymentForm()
            order_form = OrderForm()
            
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
