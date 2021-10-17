from django.shortcuts import render
import json


# Create your views here.
def index(request):
    context = {
        'title': 'Geekshop - Главная страница',
        'description': 'Описание главное страницы'
    }
    return render(request, 'products/index.html', context)


def products(request):
    with open('/var/www/django.local/geekshop/products/fixtures/products.json', 'r') as JSON:
        json_dict = json.load(JSON)

    context = {
        'title': 'Geekshop - Каталог товаров',
        'description': 'Описание каталога товаров',
        'products': json_dict,
    }
    return render(request, 'products/products.html', context)
