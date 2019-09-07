from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Post
# Create your views here.

posts= Post.objects.all()
context={
    'posts':posts,
}
def index(request):
    # posts=get_object_or_404(BlogPost)
    # context={
    #     'posts':posts,
    # }
    return render(request, 'blog/index.html',context)

def detail(request,posts_id):
    
    return render(request, 'blog/detail.html',context)
   
