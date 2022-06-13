from datetime import datetime
from nanoid import generate

class Post:
    def __init__(self, content, author):
        self.id = generate()
        self.content = content
        self.author = author
        self.__date = datetime.now()
        self.likes = 0

    def get_date(self):
        return self.__date.strftime("%d/%m/%Y, %H:%M")
    
    def like(self):
        self.likes += 1
        for i in range(len(post_list)):
            if post_list[i].id == self.id:
                post_list[i] = self
                return self
        return None


    @classmethod
    def get_all(cls):
        return post_list
    
    @classmethod
    def get_ordered_by_date(self):
        return sorted(post_list, key=lambda x: x.__date, reverse=True)
    
    @classmethod
    def get_by_id(cls, id):
        for post in post_list:
            if post.id == id:
                return post
        return None
    
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