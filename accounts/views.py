from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserChangeEmailForm, UserDeleteForm
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
    orders = Order.objects.filter(customer=request.user).order_by('-id')
    return render(request, 'profile.html', {'orders': orders})




def logout(request):
    """A view that logs the user out and redirects back to the home page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')


@login_required
def order_detail_view(request,id):
    order = Order.objects.filter(id=id)
    order_items = OrderLineItem.objects.filter(order=id)
    return render(request, 'order_detail.html', {'order_items': order_items, 'id': id, 'order': order})





@login_required
def change_email_view(request):
    print('in change_email_view')
    if request.method == 'POST':
        form = UserChangeEmailForm(request.POST)
        if form.is_valid():
            print('email form is valid')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your email has successfully been updated')
            return redirect('profile')
    else:
        form = UserChangeEmailForm()
        print('email else')
    return render(request, 'profile_change_email.html', {'form': form})

@login_required
def confirm_delete_view(request):
    delete_form = UserDeleteForm(request.POST,instance=request.user)
    user = request.user
    user.delete()
    messages.success(request, "The user is deleted")            
    return redirect('home')
 


