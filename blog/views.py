from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog_list(request):
    posts = Post.objects.all()
    
    paginator = Paginator(posts, 2)
    
    print(f"Paginator: {paginator}")
    
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

    return render(request, "list.html", {"posts": posts})


def blog_detail(request, title):
    post = get_object_or_404(Post, title=title)

    return render(request, "detail.html", {"post": post})
