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

    rows = Product.objects.all()
    for row in rows:
        row.image = str(settings.MEDIA_URL) + '/' + str(row.image)

    context = {
        'title': 'Geekshop - Каталог товаров',
        'description': 'Описание каталога товаров',
        'products': rows,
    }
    return render(request, 'products/products.html', context)
