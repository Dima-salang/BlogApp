from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = "home.html"


class BlogPostPage(DetailView):
    model = Post
    template_name = "blog-post.html"


class BlogCreatePage(CreateView):
    model = Post
    template_name = 'blog-new.html'
    fields = '__all__'

class BlogUpdatePage(UpdateView):
    model = Post
    template_name = "blog-update.html"
    fields = ["title", "body"]

class BlogDeletePage(DeleteView):
    model = Post
    template_name = "blog-delete.html"
    success_url = reverse_lazy("home")




