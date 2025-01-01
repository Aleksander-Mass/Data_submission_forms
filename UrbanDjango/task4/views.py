

# Create your views here.
from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'fourth_task/home.html')



def games_view(request):
    context = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]}
    return render(request, 'fourth_task/games.html', context)



def shop(request):
    games = {
        'games': [
            'Atomic Heart',
            'Cyberpunk 2077',
            'PayDay 2',
        ]
    }
    return render(request, 'fourth_task/shop.html', games)


def cart_view(request):
    return render(request, 'fourth_task/cart.html')