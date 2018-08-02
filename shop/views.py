from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.

# create request function called index


def index(request):
    text_var = 'This is my first django app web page'
    return HttpResponse(text_var)

# Category view


def allprodcat(request, c_slug=None):
    categories_page = None
    list_products = None
    if c_slug!=None:
        categories_page = get_object_or_404(Category, slug=c_slug)
        # Gets all available products
        list_products = Product.objects.filter(category=categories_page, available=True)
    else:
        list_products = Product.objects.all().filter(available=True)
        '''Pagination code'''
    paginator = Paginator(list_products, 4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/category.html', {'category': categories_page, 'products': products})


def proddetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product': product})
