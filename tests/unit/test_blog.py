from unittest import TestCase
from blog.blog import Blog

class TestBlog(TestCase):
    def test_create_blog(self):
        b = Blog('Test Title', 'Test Author')

        self.assertEqual('Test Title', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
