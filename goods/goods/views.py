from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    return render(request, 'goods/main_page.html')


def catalog(request):
    return render(request, 'goods/catalog.html')


def login(request):
    return render(request, 'goods/login.html')


def basket(request):
    return render(request, 'goods/basket.html')


def registration(request):
    return render(request, 'goods/registration.html')