from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Страница приложения djapp")

def categories(request, catid):
    return HttpResponse(f"<h1>Категории</h1><p>{catid}</p>")
