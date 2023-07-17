from django.shortcuts import (
    render,
    get_object_or_404,
    HttpResponse,
    redirect,
    HttpResponseRedirect,
    reverse)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from products.models import Product


@login_required
def wishlist(request):
    """
    View wishlist
    """
    wishlist_items = Wishlist.objects.filter(user=request.user)
    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request):
    """
    Add to wishlist
    """
    if request.method == 'POST':
        product_id = request.POST.get('product-id')
        product = get_object_or_404(Product, id=product_id)
        redirect_url = request.POST.get('my_redirect_url')
        try:
            wish_item = Wishlist.objects.get(
                user=request.user,
                product=product)
            if wish_item:
                messages.info(request, f'{wish_item.product} already on a wishlist')
        except Wishlist.DoesNotExist:
            Wishlist.objects.create(user=request.user, product=product)
            messages.success(request, f'{product.name} added to wishlist')

        return HttpResponseRedirect(redirect_url)

    return redirect('products')


@login_required
def remove_from_wishlist(request):
    """
    Remove from wishlist
    """
    if request.method == 'POST':
        item_id = request.POST.get('item-id')
        wish_item = get_object_or_404(Wishlist, pk=item_id)
        wish_item.delete()
        messages.success(request, f'{wish_item.product.name} deleted from wishlist')
    return HttpResponseRedirect(reverse('wishlist'))
