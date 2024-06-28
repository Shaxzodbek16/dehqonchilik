from django.shortcuts import render
from .models import Store, Product, News, Contact


def news(request):
    info = News.objects.all()
    context = {'info': info}
    return render(request, 'index.html', context=context)


def store(request):
    info = Store.objects.all()
    context = {'info': info}
    return render(request, 'store.html', context=context)


def product(request):
    info = Product.objects.all()
    context = {'info': info}
    return render(request, 'product.html', context=context)


def contact(request):
    return render(request, 'contact.html')