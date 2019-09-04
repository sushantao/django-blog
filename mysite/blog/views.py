from django.shortcuts import render, get_object_or_404


from .models import BlogPost
# Create your views here.


def index(request):
    # posts=get_object_or_404(BlogPost)
    posts= BlogPost.objects.all()
    context={
        'posts':posts,
    }
    return render(request, 'blog/index.html',context)

def detail(request,article_id):
    return render(request, 'blog/detail.html')
