from django.shortcuts import render
from .models import Post

def posted(request):
    posts = Post.objects.all()
    return render(request, 'home.html',{'posts':posts})
