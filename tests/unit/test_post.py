from unittest import TestCase
from blog.post import Post


class TestPost(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test content', p.content)

    def test_json(self):
        p = Post('Test', 'Test content')
        expected = {
            'title': 'Test',
            'content': 'Test content',
        }

        self.assertDictEqual(expected, p.json())
        
    def test_repr(self):
        p = Post('Test', 'Test content')

        self.assertEqual(p.__repr__(), "<Post title='Test', content='Test content'>")
