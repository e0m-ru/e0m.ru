from django.http import Http404
from django.shortcuts import render


def index(request):   
    context = {
        'title': 'Бабушкин А.В. e0m.ru'
    }
    return render(request, 'e0m/index.html', context)
