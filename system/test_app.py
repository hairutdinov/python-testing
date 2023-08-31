from unittest import TestCase
from unittest.mock import patch
import blog.app as app
from blog.blog import Blog


class TestApp(TestCase):
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

