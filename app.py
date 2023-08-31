from blog import Blog
from post import Post


MENU_PROMPT = "Enter 'c' to create blog, 'l' to list blogs, 'r' to read one, 'p' to create a post, or 'q' to quit."
blogs = dict()  # blog_name: blog_object


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for blog_name, blog in blogs.items():
        print('- {}'.format(blog))


def ask_create_blog():
    title = input('Enter blog title: ')
    author = input('Enter your name: ')
    blogs[title] = Blog(title, author)


def ask_read_blog():
    pass


def ask_create_post():
    pass
