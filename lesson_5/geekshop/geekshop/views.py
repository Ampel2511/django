from django.shortcuts import render
from mainapp.models import Product


def main(request):
    title = 'главная'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    products = Product.objects.all()[:4]
    basket = request.user.basket.all()
    total_quantity = 0
    for item in basket:
        total_quantity += item.quantity
    context = {
        'title': title,
        'links_page': links_page,
        'products': products,
        'total_quantity': total_quantity,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'контакты'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    basket = request.user.basket.all()
    total_quantity = 0
    for item in basket:
        total_quantity += item.quantity
    context = {
        'title': title,
        'links_page': links_page,
        'total_quantity': total_quantity,
    }
    return render(request, 'geekshop/contact.html', context=context)

