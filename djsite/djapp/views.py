from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("Страница приложения djapp")

def categories(request, catid):
    return HttpResponse(f"<h1>Категории</h1><p>{catid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
