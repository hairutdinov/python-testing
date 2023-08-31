MENU_PROMPT = "Enter 'c' to create blog, 'l' to list blogs, 'r' to read one, 'p' to create a post, or 'q' to quit."
blogs = dict() # blog_name: blog_object


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)



def print_blogs():
    for blog_name, blog in blogs.items():
        print('- {}'.format(blog))

