from django.shortcuts import render, redirect
from .models import Store, Product, News, Contact
from django.http import HttpResponse


def news(request):
    info = News.objects.all()
    context = {'info': info}
    return render(request, 'index.html', context=context)


def store(request):
    info = Store.objects.all()
    context = {'info': info}
    return render(request, 'store.html', context=context)


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product.html', context=context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        telephone = request.POST.get('telephone')
        purpose = request.POST.get('purpose')
        text = request.POST.get('message')
        information = Contact(name=name, telephone=telephone, purpose=purpose, text=text)
        information.save()
        return redirect('confirm')
    return render(request, 'contact.html')


def confirm(request):
    return render(request, 'confirm.html')


def _404(request):
    return render(request, '404.html', status=404)
