from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-pub_date')

    context = {
        'posts': posts
    }
    return render(request, 'posts/post_list.html', context)

def posted_by(request, id):
    posts = Post.objects.filter(posted_by__id=id)

    context = {
        'posts': posts
    }
    return render(request, 'posts/posted_by.html', context)