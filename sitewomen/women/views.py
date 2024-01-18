from django.shortcuts import render
from django.http import HttpResponse

# dfdfdfdf
def index(request):
    return HttpResponse("Страница приложения women")


def categories(request):
    return HttpResponse("<h1>Cтатьи по категориям</h1>")