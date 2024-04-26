from django.shortcuts import render, get_object_or_404
from .models import Post

def posted(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'home.html',{'posts':posts})
# slug_url)
def post_detail(request,slug_url) :
    post = Post.objects.get(slug = slug_url) 
    """slug=slug_url"""
    return render(request, 'postdt.html',{'post':post})