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
        return ''
