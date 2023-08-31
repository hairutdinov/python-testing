from unittest import TestCase
from blog.blog import Blog
from blog.post import Post


class TestBlog(TestCase):
    def test_create_post(self):
        b = Blog('Test Title', 'Test Author')
        b.create_post('Post title', 'Post content')

        self.assertEqual(1, len(b.posts))
        self.assertEqual('Post title', b.posts[0].title)
        self.assertEqual('Post content', b.posts[0].content)

    def test_json_with_posts(self):
        b = Blog('Test Title', 'Test Author')
        b.create_post('Post title', 'Post content')

        expected = {
            'title': 'Test Title',
            'author': 'Test Author',
            'posts': [
                {
                    'title': 'Post title',
                    'content': 'Post content',
                }
            ]
        }

        self.assertDictEqual(expected, b.json())
