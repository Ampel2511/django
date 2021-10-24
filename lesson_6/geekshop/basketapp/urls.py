from django.urls import path
import basketapp.views as cart

app_name = 'basketapp'
urlpatterns = [
    path('', cart.basket, name='view'),
    path('add/<int:pk>/', cart.add, name='add'),
    path('remove/<int:pk>/', cart.remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', cart.basket_edit, name='edit'),
]
