from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def index(request):
    posts=Post.objects.all()
    context={
        'posts':posts,
    }
    return render(request, 'blog/index.html',context)

def detail(request,posts_id):
    post = get_object_or_404(Post, pk= posts_id)
    return render(request, 'blog/detail.html',{'post':post})
   