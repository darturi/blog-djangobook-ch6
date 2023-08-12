from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)


urlpatterns = [
    # Add url for post creation page
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    # Add urls to look at individual posts
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    # Add url for post update page
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    # Add url for post deletion
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    # Add url for the home page of blog
    path("", BlogListView.as_view(), name="home"),
]
