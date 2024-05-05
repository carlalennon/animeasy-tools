from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.
def profile(request):
    """ Display user profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    
    form = UserProfileForm(instance=profile)
    template = 'profiles/profile.html'
    orders = profile.orders.all()
    
    context = {
        'form': form,
        'profile': profile,
        'orders' : orders,
    }
    
    return render(request, template, context)   