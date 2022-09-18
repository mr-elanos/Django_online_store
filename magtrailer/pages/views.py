from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *


def index(request):
    return HttpResponse('Main page')


def categories(request, catid):
    return HttpResponse(f'<h1>Categories {catid}</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена :(</h1>')
