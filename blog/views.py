from django.shortcuts import render
from .models import Post  # import from models.py file
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.


# A view for the homepage
class BlogListView(ListView):
    # the very same model we just imported, have to know what data we are
    # formatting according to the generic view we just imported, and set the
    # model class attribute (inherited from the generic ListView) to Post
    model = Post

    # Then we clarify that that BlogListView will use the "home.html" file as
    # a guide to its specific layout
    template_name = "home.html"


# a view for looking at a given specific post
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


# a view for post creation
class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

    # Note: a redirect url is not necessary for this view despite there being
    # a redirect after posting a post becuase by defualt django will use
    # get_absolute_url() on the object


# a view for updating / editing posts that are already posted
class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]  # becuase author can't change


# a view for deleting posted posts
class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")  # where to redirect user after deleting post
