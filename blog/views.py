from django.shortcuts import render
from .models import Post
from django.utils import timezone
__author__='admin'


def post_list(request):
  #  posts = Post.objects.filter(author=admin) #zmienna post, nazwa naszego querysetu
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


