from blog.post import Post


class Blog:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.posts = []

    def create_post(self, title, content):
        pass

    def json(self):
        pass

    def __repr__(self) -> str:
        posts_count = len(self.posts)
        return '{} by {} ({} post{})'.format(self.title, self.author, posts_count, ('s' if posts_count != 1 else ''))
