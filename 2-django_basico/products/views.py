from django.shortcuts import render
from django.http import HttpResponse

def get_products(request):
    return render(request, "products/index.html")


def insert_product(request):
    return HttpResponse("")