from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.views.defaults import page_not_found

def index(request):   
    context = {
        'title': 'Бабушкин А.В. e0m.ru'
    }
    return render(request, 'e0m/index.html', context)


def __404__(request):
    return page_not_found(request, 'page not found')
