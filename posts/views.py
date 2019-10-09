from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm


def post_list(request):
    """ Lists all posts in the site """
    posts = Post.objects.order_by('-pub_date').filter(is_published=True)

    context = {
        'posts': posts
    }
    return render(request, 'posts/post_list.html', context)

def posted_by(request, id):
    """ Lists all posts done by the specified user """
    posts = Post.objects.filter(posted_by__id=id)

    context = {
        'posts': posts
    }
    return render(request, 'posts/posted_by.html', context)

@login_required
def new_post(request):
    """ Creates a new post """
    user = request.user

    form = PostForm(
        request.POST or None,
        initial={'posted_by': user.id}
    )

    context = {
        'form': form
    }

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('index')
    else:
        messages.error(request, 'Invalid post')

    return render(request, 'posts/new_post.html', context)