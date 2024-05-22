from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    # MAIN
    path('', views.index, name='index'),
    path('log', views.log, name='log'),
    path('video', views.video, name='video'),
    path('ctspi', views.ctspi, name='ctspi'),
    # POST CRUD
    path('post_create', views.post_create, name='post_create'),
    path('post_read/<int:post_ID>', views.post_read, name='post_read'),
    path('post_update/<int:post_ID>', views.post_update, name='post_update'),
    path('post_delete/<int:post_ID>', views.post_delete, name='post_delete'),
    # ALL OTHERS
    re_path(r'.*', views.__404__, name='404'),
]
