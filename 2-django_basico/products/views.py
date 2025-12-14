from django.shortcuts import render
from django.http import HttpResponse

products = [
    
]

def get_products(request):
    return render(request, "products/index.html")


def insert_product(request):
    return render(request, "formProducts/index.html")


def post_product(request, product):
    products.append(product)