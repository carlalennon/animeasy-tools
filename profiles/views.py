"""
View for profile app
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


User = get_user_model()

@login_required
def profile(request):
    """ Display user profile """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    orders = profile.orders.all()
    has_orders = orders.exists()

    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
        'has_orders': has_orders,
    }

    return render(request, template, context)

def order_history(request, order_number):
    """ Display order history """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        #'from_profile': True,
    }

    return render(request, template, context)

@login_required
def delete_profile(request):
    """Delete user profile."""
    user_profile = get_object_or_404(UserProfile, user=request.user)
    profile.delete()
    user_profile.delete()
    messages.success(request, 'Your profile has been deleted. Come back any time.')
    return redirect('home')
