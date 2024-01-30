from django.shortcuts import render
from .helpers import COLOR
from .forms import PostForm
from .models import PostModel


def post_create(request):
    form = PostForm()
    context = {
        'title': 'Create post - e0m.ru',
        'color': COLOR(),
        'form': form,
    }
    return render(request, 'posts_CRUD/post_create.html', context)


def post_read(request, post_ID):
    context = {
        'title': f'Read post {post_ID} - e0m.ru',
        'color': COLOR(),
    }
    return render(request, 'posts_CRUD/post_read.html', context)


def post_update(request, post_ID):
    context = {
        'title': f'Update post {post_ID} - e0m.ru',
        'color': COLOR(),
    }
    return render(request, 'posts_CRUD/post_update.html', context)


def post_delete(request, post_ID):
    context = {
        'title': f'Delete post {post_ID} - e0m.ru',
        'color': COLOR(),
    }
    return render(request, 'posts_CRUD/post_delete.html', context)
