from unittest import TestCase
from blog import Blog
from post import Post


class TestBlog(TestCase):
    def test_create_blog(self):
        b = Blog('Test Title', 'Test Author')

        self.assertEqual('Test Title', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test Title', 'Test Author')

        self.assertEqual(b.__repr__(), 'Test Title by Test Author (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test Title', 'Test Author')
        b2 = Blog('Test Title 2', 'Test Author 2')

        p = Post('Test', 'Test content')
        p2 = Post('Test 2', 'Test content 2')

        b.posts.append(p)
        b2.posts.append(p)
        b2.posts.append(p2)

        self.assertEqual(b.__repr__(), 'Test Title by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'Test Title 2 by Test Author 2 (2 posts)')

    def test_json(self):
        b = Blog('Test Title', 'Test Author')

        expected = {
            'title': 'Test Title',
            'author': 'Test Author',
            'posts': []
        }

        self.assertDictEqual(expected, b.json())
