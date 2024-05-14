import subprocess
from random import choice
import os

def COLOR():
    blue = ['0099CC', 'F68D85', 'C2254D', '4ACBF7', '236175']
    red = ['c8374f', 'E547F5', 'C2BA25', 'F78D9E', '75434B' ]
    green = ['079f8d', 'F685B7', 'C225B8', '54F7E4', '638F8A']
    color_scheme= dict(zip(['main','second', 'opposite', 'light', 'dark'], choice((blue, red, green))))
    return color_scheme

def get_log():
    acces_log = subprocess.Popen(['tail', '/var/log/nginx/access.log'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    acces_log = acces_log.stdout.readlines()
    acces_log = map(lambda x: x.decode("utf-8"), acces_log)

    error_log = subprocess.Popen(['tail', '/var/log/nginx/error.log'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    error_log = error_log.stdout.readlines()
    error_log = map(lambda x: x.decode("utf-8"), error_log)

    return {'acces_log':acces_log,'error_log': error_log}

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
       ip = x_forwarded_for.split(',')[0]
    else:
       ip = request.META.get('REMOTE_ADDR')
    return ip