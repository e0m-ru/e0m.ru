from django.shortcuts import render
from e0m.helpers import COLOR
from django.http.request import HttpRequest
import os
from django.conf import settings
import subprocess


def tesseract(fp):
    data = subprocess.getoutput(
        f'tesseract -l rus {fp} stdout')
    return data


def handle_uploaded_file(f):
    fp = f'{settings.MEDIA_ROOT}tesseract/{f.name}'
    fu = f'{settings.MEDIA_URL}tesseract/{f.name}'
    descriptor = os.open(
        path= fp,
        flags=(
            os.O_WRONLY  # access mode: write only
            | os.O_CREAT  # create if not exists
            |os.O_TRUNC  # truncate the file to zero
        ),
        mode=0o777
    )
    with open(descriptor, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return fu

def tess(request):
    context = {
        'title': 'tesseract-e0m.ru',
        'color': COLOR(),
    }

    if request.method == 'POST':
        fl = request.FILES['file']
        fu = handle_uploaded_file(fl)
        text = tesseract(f'{settings.MEDIA_ROOT}tesseract/{fl.name}')
        context.update({'text': text})
        context.update({'img': fu})
        context.update({'title': 'tesseract-results-e0m.ru'})
        return render(request, 'tess/tess_res.html', context)
    return render(request, 'tess/tess.html', context)
