from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def blog_list(request):
    posts = Post.objects.all()

    return render(request, "list.html", {"posts": posts})


def blog_detail(request, title):
    post = get_object_or_404(Post, title=title)

    return render(request, "detail.html", {"post": post})
