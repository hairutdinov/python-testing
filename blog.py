from post import Post
from typing import List

class Blog:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.posts: List[Post] = []

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self) -> dict:
        return {
            'title': self.title,
            'author': self.author,
            'posts': [p.json() for p in self.posts],
        }

    def __repr__(self) -> str:
        posts_count = len(self.posts)
        return '{} by {} ({} post{})'.format(self.title, self.author, posts_count, ('s' if posts_count != 1 else ''))
