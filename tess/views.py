from django.shortcuts import render
from e0m.helpers import COLOR
from django.http.request import HttpRequest
import os
from django.conf import settings
import subprocess
import time 
# os._wrap_close.


def tesseract(fp):
    # acces_log = subprocess.Popen(['docker', 'run', '--rm','-i', '-v', '/var/www/djangoproject/media/tesseract/:/app', '-w', '/app', 'minidocks/tesseract:5-rus', '-l rus+eng', f'{fp}' , f'{fp}' ],
    #                              stdout=subprocess.PIPE,
    #                              stderr=subprocess.STDOUT)
    # acces_log = acces_log.stdout.read().decode(encoding='utf-8')
    data = subprocess.getoutput(
        f'docker run --rm -i -v /var/www/djangoproject/media/tesseract:/app -w /app minidocks/tesseract:5-rus -l rus+eng "{fp}" stdout')

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
        text = tesseract(f'{fl.name}')
        context.update({'text': text})
        context.update({'img': fu})
        context.update({'title': 'tesseract-results-e0m.ru'})
        return render(request, 'tess/tess_res.html', context)
    return render(request, 'tess/tess.html', context)
