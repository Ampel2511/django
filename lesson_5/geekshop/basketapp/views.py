from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    title = 'корзина'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    basket = request.user.basket.all()
    total_value = 0

    for item in basket:
        total_value += item.product.price

    context = {
        'title': title,
        'links_page': links_page,
        'basket': basket,
        'total_value': total_value,
    }
    return render(request, 'basketapp/basket.html', context)


def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()
    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request):
    Basket.objects.all().delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
