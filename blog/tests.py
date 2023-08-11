from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse

# Create your tests here.


class BlogTests(TestCase):
    # set up data for a test user and a test Post
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="test_user", email="test@email.com", password="secret"
        )

        cls.post = Post.objects.create(
            title="A good title", body="Nice body content", author=cls.user
        )

    # Tests to make sure that the content of the user and post are accurate
    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "test_user")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    # Tests if the homepage exists at the correct url
    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # Tests if the example post created in setUpTestData() exists at the correct url
    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("home"))

        # Test that url name works
        self.assertEqual(response.status_code, 200)

        # test that correct content is included on the home page
        self.assertContains(response, "Nice body content")

        # test that home page uses correct template
        self.assertTemplateUsed(response, "home.html")

    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000000/")

        # Test that url name works
        self.assertEqual(response.status_code, 200)

        # Test that fake url name fails
        self.assertEqual(no_response.status_code, 404)

        # test that test post page contains proper information
        self.assertContains(response, "A good title")

        # test that test post page uses correct template
        self.assertTemplateUsed(response, "post_detail.html")
