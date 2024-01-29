from django.contrib import admin
from django.urls import path, re_path, include
from django.http.response import HttpResponseNotFound

urlpatterns = [
    path('admin/assa', admin.site.urls),
    path('tess', include('tess.urls')),
    path('', include('e0m.urls')),
]
