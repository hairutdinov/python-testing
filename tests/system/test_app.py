from unittest import TestCase
from unittest.mock import patch
import app as app
from blog import Blog
from post import Post


class TestApp(TestCase):
    def setUp(self) -> None:
        blog = Blog('Test', 'Test Author')
        app.blogs[blog.title] = blog

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test', 'Test Author', 'q')
            app.menu()
            self.assertIsNotNone(app.blogs.get('Test'))

    # or check if ask_create_blog() function was called
    # def test_menu_calls_create_blog(self):
    #     with patch('builtins.input') as mocked_input:
    #         with patch('app.ask_create_blog') as mocked_create_blog:
    #             mocked_input.side_effect = ('c', 'Test Title', 'Test Author', 'q')
    #             app.menu()
    #             mocked_create_blog.assert_called()

    def test_menu_calls_read_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('r', 'Test Title', 'q')
            with patch('app.ask_read_blog') as mocked_read_blog:
                app.menu()
                mocked_read_blog.assert_called()

    def test_menu_calls_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p', 'Test Title', 'q')
            with patch('app.ask_create_post') as mocked_create_post:
                app.menu()
                mocked_create_post.assert_called()

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    @patch('builtins.input', return_value='q')
    def test_menu_prints_prompt(self, mocked_input):
        app.menu()
        mocked_input.assert_called_with(app.MENU_PROMPT)

    # def test_print_blogs(self):
    #     b = Blog('Test Blog', 'Test Author')
    #     app.blogs = {'Test': b}
    #     with patch('builtins.print') as mocked_print:
    #         app.print_blogs()
    #         mocked_print.assert_called_with('- Test Blog by Test Author (0 posts)')
    @patch('builtins.print')
    def test_print_blogs(self, mocked_print):
        app.print_blogs()
        mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            # mocked_input.assert_called_with('Enter blog title: ')
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        b = app.blogs['Test']
        with patch('builtins.input', return_value='Test') as mocked_input:
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(b)

    def test_print_posts(self):
        b = app.blogs['Test']
        b.create_post('Test Post', 'Test Content')
        app.blogs[b.title] = b

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(b)
            mocked_print_post.assert_called_with(b.posts[0])

    def test_print_post(self):
        p = Post('Test Post', 'Test Content')

        with patch('builtins.print') as mocked_print:
            app.print_post(p)
            expected_print = '''
--- Test Post ---

Test Content

'''
            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Post', 'Test Content')
            app.ask_create_post()

            self.assertEqual('Test Post', app.blogs['Test'].posts[0].title)
            self.assertEqual('Test Content', app.blogs['Test'].posts[0].content)
