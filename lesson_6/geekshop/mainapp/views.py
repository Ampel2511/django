import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    product = Product.objects.all()
    return random.sample(list(product), 1)[0]


def get_same_product(hot_product):
    same_product = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_product


def products(request, pk=None):
    title = 'каталог'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all()[:8]
    basket = get_basket(request.user)
    hot_product = get_hot_product()
    same_product = get_same_product(hot_product)
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'Все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        context = {
            'title': title,
            'links_menu': links_menu,
            'links_page': links_page,
            'products': products,
            'category': category,
            'basket': basket,
            'hot_product': hot_product,
            'same_product': same_product,
        }
        return render(request, 'mainapp/category_products.html', context=context)
    context = {
        'title': title,
        'links_menu': links_menu,
        'links_page': links_page,
        'products': products,
        'basket': basket,
        'hot_product': hot_product,
        'same_product': same_product,
    }
    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    basket = get_basket(request.user)
    product = get_object_or_404(Product, pk=pk)
    title = f'{product.name}'
    context = {
        'title': title,
        'links_page': links_page,
        'basket': basket,
        'product': product,
    }

    return render(request, 'mainapp/product.html', context=context)
