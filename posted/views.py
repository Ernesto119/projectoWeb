from django.shortcuts import render, get_object_or_404
from .models import Post

def posted(request):
    posts = Post.objects.all()
    return render(request, 'home.html',{'posts':posts})

def post_detail(request, slug_url):
    post = Post.objects.get(slug=slug_url)
    return render(request, 'postdt.html',{'post':post})