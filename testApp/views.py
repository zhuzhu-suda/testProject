from rest_framework import generics
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .serializers import PostSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def home(request):
    return HttpResponse("welcome to Django! API address：<a href='/api/posts/'>/api/posts/</a>")

def post_list(request):
    """for XSS test"""
    posts = Post.objects.all()
    return render(request, "list.html",{"posts":posts})

def post_create(request):
    """for CSRF test"""
    if request.method == "POST":
        content = request.POST.get("content")
        Post.objects.create(content=content)
        return redirect("post_list")
    return render(request, "create.html")