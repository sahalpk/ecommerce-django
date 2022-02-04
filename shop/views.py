from django.shortcuts import render, get_object_or_404
from .models import product, Category
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.


def allProdCat(request, c_slug=None):
    cat = None
    products_list = None
    paginator = None
    if c_slug != None:
        cat = get_object_or_404(Category, slug=c_slug)
        products_list = product.objects.all().filter(category=cat, available=True)
    else:
        products_list = product.objects.all().filter(available=True)
        paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = Paginator(products_list, 6).page(page)
    except (EmptyPage, InvalidPage):
        products = Paginator(products_list, 6).page(
            Paginator(products_list, 6).num_pages)
    return render(request, 'category.html', {'category': cat, 'products': products})


def proDetail(request, c_slug, product_slug):
    try:
        Products = product.objects.get(
            category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'Product': Products})
