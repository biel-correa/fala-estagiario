from app import app
from flask import request

from model.Post import Post

@app.route('/post', methods=['POST'])
def save_post():
    content = request.form['content']
    author = request.form['author']
    post = Post.save(content, author)
    if post:
        return 'Postagem salva com sucesso!', 200
    return 'Erro ao salvar postagem', 500