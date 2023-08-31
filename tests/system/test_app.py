from unittest import TestCase
from unittest.mock import patch
import app as app
from blog import Blog


class TestApp(TestCase):
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
        b = Blog('Test Blog', 'Test Author')
        app.blogs = {'Test': b}
        app.print_blogs()
        mocked_print.assert_called_with('- Test Blog by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            # mocked_input.assert_called_with('Enter blog title: ')
            self.assertIsNotNone(app.blogs.get('Test'))

