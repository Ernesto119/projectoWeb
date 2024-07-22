from django.shortcuts import render,redirect
from .models import Post
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

def sign_up(request):
    pass

def sign_in(request):
    pass

def exit(request):
    logout(request)
    return redirect("")

def home(request):
    posts = Post.objects.all().order_by("-id")
    return render(request, "home.html", {"posts": posts})


# slug_url)
def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except:
        raise Http404()

    return render(request, "postdt.html", {"post": post})


def error_page(request,exception):
    return render(request, "404_error.html")
