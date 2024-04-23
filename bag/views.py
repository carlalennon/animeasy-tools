from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_bag(request):
    """ Returns user bag """
    return render(request, 'bag/bag.html')

## From Boutique Ado 
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

 
def adjust_bag(request, item_id):
    """ Adjust quantity of product from bag.html """
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    
    print("Made it to views!")  # This will print the updated bag to the console

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """ Remove item from shopping bag """
    
    try:
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag.pop(item_id)
            
        request.session['bag'] = bag
        return HttpResponse(status=200)
    
    except Exception as e: 
        return HttpResponse(status=500)