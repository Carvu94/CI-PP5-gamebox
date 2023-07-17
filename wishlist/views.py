from django.shortcuts import render

from .models import Wishlist


def wishlist(request):
    """
    view to render the wishlist page
    """
    wishlist_items = Wishlist.objects.filter(user=request.user)
    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, template, context)
