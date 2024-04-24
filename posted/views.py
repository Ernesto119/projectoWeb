from django.shortcuts import render, get_object_or_404
from .models import Post

def posted(request):
    posts = Post.objects.all()
    return render(request, 'home.html',{'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'postdt.html',{'post':post})