from django.shortcuts import get_object_or_404, render

from store.models import Product
from category.models import Category


def store(request, cat_slug=None):
    products = None
    category = None

    if cat_slug != None:
        category = get_object_or_404(Category, slug__iexact=cat_slug)
        products = Product.objects.filter(category=category, is_available=True)
        products_count = products.count()

    else:
        products = Product.objects.filter(is_available=True)
        products_count = products.count()

    ctx = {"products": products, "products_count": products_count, "category": category}

    return render(request, "store/store.html", context=ctx)


def product_detail(request, product_slug=None, cat_slug=None):
    try:
        product = Product.objects.get(category__slug=cat_slug, slug__iexact=product_slug)
    except Exception as e:
        raise e
    context = {'obj':product}
    return render(request, 'store/product_detail.html', context)
