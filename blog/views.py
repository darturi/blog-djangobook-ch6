from django.shortcuts import render
from .models import Post  # import from models.py file
from django.views.generic import ListView, DetailView


# Create your views here.
class BlogListView(ListView):
    # the very same model we just imported, have to know what data we are
    # formatting according to the generic view we just imported, and set the
    # model class attribute (inherited from the generic ListView) to Post
    model = Post

    # Then we clarify that that BlogListView will use the "home.html" file as
    # a guide to its specific layout
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
