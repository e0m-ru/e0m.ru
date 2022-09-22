from django.shortcuts import render
from django.views.defaults import page_not_found
from random import choice
import os, io
import subprocess

def index(request):
    out = subprocess.Popen(['tail', '/var/log/nginx/access.log'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    out = out.stdout.readlines()
    out = map(lambda x: x.decode("utf-8"),out)

    out2 = subprocess.Popen(['tail', '/var/log/nginx/error.log'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    out2 = out2.stdout.readlines()
    out2 = map(lambda x: x.decode("utf-8"),out2)

    context = {
        'title': 'Бабушкин А.В. e0m.ru',
        'color': choice(os.listdir('static/css/colors/')),
        'request': request,
        'STDOUT_acces': out,
        'STDOUT_error': out2,
    }
    return render(request, 'e0m/index.html', context)


def __404__(request):
    return page_not_found(request, 'page not found')
