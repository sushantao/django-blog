from django.urls import include, path
from . import views


app_name='blog'
urlpatterns = [
    #ex: /blog/
    path('', views.index,name='index'),
    #ex:/blog/1
    path('<int:posts_id>/',views.detail, name='detail')
]