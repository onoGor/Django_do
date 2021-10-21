from django.shortcuts import render

#from mainapp.models import Product


def main(request):
    return render(request, 'geekshop/index.html')


def contacts(request):
    return render(request, 'geekshop/contact.html')

'''def main(request):
    title = 'Магазин'

    products = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'Контакты'

    context = {
        'title': title,
    }
    return render(request, 'geekshop/contact.html', context)'''