from django.urls import path
from .views import home_view, games_view, cart_view

urlpatterns = [
    path('', home_view, name='home'),
    path('games/', games_view, name='games'),
    path('cart/', cart_view, name='cart'),
]
