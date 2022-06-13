from datetime import datetime

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.__date = datetime.now()
        self.likes = 0

    def get_date(self):
        return self.__date.strftime("%d/%m/%Y, %H:%M")

    @classmethod
    def get_all(cls):
        return post_list
    
    @classmethod
    def save(cls, content, author):
        if len(content) > 200:
            raise ValueError("Conteúdo muito grande")
        post = Post(content, author)
        post_list.append(post)
        return post


post_list = [
    Post('Hello, world!', 'Augusto'),
    Post('Wow uma postagem', 'Pedro')
]