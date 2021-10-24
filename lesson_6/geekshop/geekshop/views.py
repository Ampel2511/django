from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product
from mainapp.views import get_basket


def main(request):
    title = 'главная'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    products = Product.objects.all()[:4]
    basket = get_basket(request.user)
    context = {
        'title': title,
        'links_page': links_page,
        'products': products,
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'контакты'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    basket = get_basket(request.user)
    context = {
        'title': title,
        'links_page': links_page,
        'basket': basket,
    }
    return render(request, 'geekshop/contact.html', context=context)

