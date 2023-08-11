from django.db import models
from django.urls import reverse

# Create your models here.

# Create a Post model that contains three fields to be initialized, the author
# of the post, the title of the post, and the body of the blog post itself
# The three fields can be thought of as columns in a data table


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    # returns a human readable representation
    def __str__(self):
        return self.title

    # Tells django how to calculate the canonical URL for our model object
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
