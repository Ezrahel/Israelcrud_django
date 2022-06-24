from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView



class PostListView():
    model=Post


class PostCreateView():
    model = Post

    fields = "__all__"

    success_url  = reverse_lazy("blog:all")

class PostDetailView():
    model = Post

class PostUpdateView():
    model = Post

    fields = "__all__"

    success_url  = reverse_lazy("blog:all")

class PostDeleteView():
    model = Post

    fields = "__all__"

    success_url  = reverse_lazy("blog:all")