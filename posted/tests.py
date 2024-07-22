from django.test import Client, TestCase
from django.urls import reverse
from .models import Post


class PostTest(TestCase):
    def setUp(self):
        self.title = "Test Post"
        self.publish_content = "This is a test post content"

    def test_post_creation(self):
        post = Post.objects.create(
            title=self.title, publish=self.publish_content, slug="test-post-2024-07-22"
        )
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.publish, "This is a test post content")
        self.assertEqual(post.slug, "test-post-2024-07-22")


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(
            title="Test Post",
            publish="This is a test post content",
        )

    def test_home(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_error_page(self):
        response = self.client.get("unexisturl")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "404_error.html")

    def test_post_detail_view_template(self):
        response = self.client.get(reverse("post_detail", args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "postdt.html")
        self.assertEqual(response.context["post"], self.post)
