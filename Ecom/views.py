from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm
from accounts.models import Profile


# Create your views here.

def product_list(request, category_slug=None):

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-id')
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    try:
        profile = Profile.objects.get_or_create(user=request.user)[0]
    except:
        profile = None
    context = {
        'category': category,
        'categories': categories, 'products': products,
        'cart_product_form': cart_product_form,
        'profile': profile,
    }
    return render(request, 'Ecom/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'Ecom/product/detail.html', context)


