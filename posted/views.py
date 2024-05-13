from django.shortcuts import render
from .models import Post
from django.http import Http404


def posted(request):
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
