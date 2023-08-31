class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        return {
            'title': self.title,
            'content': self.content,
        }

    def __repr__(self) -> str:
        return '<Post title={}, content={}>'.format(repr(self.title), repr(self.content))
