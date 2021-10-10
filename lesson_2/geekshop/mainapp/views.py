from django.shortcuts import render


def products(request):
    title = 'каталог'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'items', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    links_menu = [
        {'href': 'items', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'title': title,
        'links_menu': links_menu,
        'links_page': links_page
    }

    return render(request, 'mainapp/products.html', context=context)
