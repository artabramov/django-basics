from django.shortcuts import render
from products.models import ProductCategory, Product
from django.conf import settings


# Create your views here.
def index(request):
    context = {
        'title': 'Geekshop - Главная страница',
        'description': 'Описание главное страницы'
    }
    return render(request, 'products/index.html', context)


def products(request):

    context = {
        'title': 'Geekshop - Каталог товаров',
        'description': 'Описание каталога товаров',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
