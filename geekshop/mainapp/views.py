from django.shortcuts import render

from mainapp.models import ProductCategory, Product


def products(request, pk=None):

    title = 'каталог'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all()[:4]
    context = {
        'title': title,
        'links_menu': links_menu,
        'links_page': links_page,
        'products': products,
    }
    print(pk)
    return render(request, 'mainapp/products.html', context=context)
