blogs = dict() # blog_name: blog_object


def menu():
    print_blogs()


def print_blogs():
    for blog_name, blog in blogs.items():
        print('- {}'.format(blog))

