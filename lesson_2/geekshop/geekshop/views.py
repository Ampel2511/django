from django.shortcuts import render


def main(request):
    title = 'главная'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'items', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    context = {
        'title': title,
        'links_page': links_page
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'контакты'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'items', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    context = {
        'title': title,
        'links_page': links_page
    }
    return render(request, 'geekshop/contact.html', context=context)

