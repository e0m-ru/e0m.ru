from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.views.defaults import page_not_found
from random import choice
import os
import sys


def index(request):
    styles_list = 1
    context = {
        'title': 'Бабушкин А.В. e0m.ru',
        'style': choice(os.listdir('/var/www/djangoproject/static/css/colors/'))
    }
    return render(request, 'e0m/index.html', context)


def __404__(request):
    return page_not_found(request, 'page not found')
