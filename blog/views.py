from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):
    # posts = Post.objects.filter(title__contains='title')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})