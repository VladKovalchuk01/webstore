from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    return render(request, 'main_page/main_page.html')


def catalog(request):
    return render(request, 'main_page/catalog.html')


def login(request):
    return render(request, 'main_page/login.html')
