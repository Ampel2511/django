from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product


def products(request, pk=None):
    title = 'каталог'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all()[:8]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    total_quantity = 0
    for item in basket:
        total_quantity += item.quantity
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
            'total_quantity': total_quantity,
        }
        return render(request, 'mainapp/category_products.html', context=context)
    context = {
        'title': title,
        'links_menu': links_menu,
        'links_page': links_page,
        'products': products,
        'basket': basket,
        'total_quantity': total_quantity,
    }
    return render(request, 'mainapp/products.html', context=context)
