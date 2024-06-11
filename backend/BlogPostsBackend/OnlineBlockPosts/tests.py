from django.test import TestCase

from OnlineBlockPosts.models import Post


# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Title", slug="test-slug")

    def test_can_retrieve_post_by_slug(self):
        post = Post.objects.get(slug=self.post.slug)
        self.assertEqual(post.title, "Test Title")