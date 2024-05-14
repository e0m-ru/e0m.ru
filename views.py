from django.shortcuts import render
from django.views.defaults import page_not_found
from django.conf.global_settings import STATIC_ROOT, STATIC_URL
from .helpers import get_log, COLOR, get_client_ip
from .posts_CRUD import *


def log(request):
    logs = get_log()
    context = {
        'title': 'AAAAAA Log - e0m.ru',
        'color': COLOR(),
        'STDOUT_acces': logs['acces_log'],
        'STDOUT_error': logs['error_log'],
    }
    return render(request, 'e0m/log.html', context)


def index(request):
    context = {
        'title': 'Бабушкин А.В. e0m.ru',
        'color': COLOR(),
        'ip': get_client_ip(request),
    }
    return render(request, 'e0m/index.html', context)



def video(request):
    context = {
        'title': 'Бабушкин А.В. e0m.ru',
        'color': COLOR(),
    }
    return render(request, 'e0m/video.html', context)

def __404__(request):
    return page_not_found(request, 'page not found')
