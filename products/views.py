from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from .models import Product, Console
from .forms import ProductForm
from profiles.models import UserProfile
from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.


def all_products(request):
    """ Show all products, sort and search """

    products = Product.objects.all()
    query = None
    consoles = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'console':
                sortkey = 'console__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'console' in request.GET:
            consoles = request.GET['console'].split(',')
            products = products.filter(console__name__in=consoles)
            consoles = Console.objects.filter(name__in=consoles)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_console': consoles,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    review_form = ReviewForm(data=request.POST)

    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.product = product
        review.save()
    else:
        review_form = ReviewForm()

    return render(request, 'products/product_detail.html',
                  {'product': product,
                   'reviews': reviews,
                   'review_form': ReviewForm(),
                   })


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfuly added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please \
                            ensure the form is valid.')
    else:
        form = ProductForm()

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please \
                            ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """
    Add a product review
    """
    product = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Review.objects.create(author=user,
                                  product=get_object_or_404
                                  (Product, pk=product_id),
                                  content=content)
            messages.success(request, 'Your review has been \
                successfully added.')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'There is an error. Please try again.')
    else:
        form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
