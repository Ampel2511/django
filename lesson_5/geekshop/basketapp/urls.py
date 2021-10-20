from django.urls import path
import basketapp.views as cart

app_name = 'basketapp'
urlpatterns = [
    path('', cart.basket, name='view'),
    path('add/<int:pk>/', cart.add, name='add'),
    path('remove/', cart.remove, name='remove'),
]
