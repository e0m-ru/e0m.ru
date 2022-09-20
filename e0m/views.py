from django.http import HttpResponse


def index(request):
    return HttpResponse("e0m.ru")