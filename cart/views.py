from django.shortcuts import render, redirect, reverse
from django.contrib import messages


# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    if request.session.get('cart'):
        cart = request.session.get('cart')
        return render(request, "cart.html")
    else:
        messages.info(request, 'Your CART is empty, let''s go shopping!')
        return redirect('product-list-all')

def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_item_in_cart(request, id):
    """
    Delete the item from cart
    """
    
    cart = request.session.get('cart', {})

    cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))