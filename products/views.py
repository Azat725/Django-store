from django.shortcuts import render

def index(request):
    context = {
        "title": "Magazine",
        "is_promition": False,
    }
    return render(request, 'products/index.html', context)

def products(request):
    return render(request, 'products/products.html')