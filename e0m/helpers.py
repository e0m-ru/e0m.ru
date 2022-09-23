import subprocess
from random import choice
import os

def COLOR():
    return choice(('0099CC','079f8d','c8374f','b1358a',))

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