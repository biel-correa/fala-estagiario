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

@app.route('/post/like', methods=['POST'])
def like_post():
    id = request.args['id']
    post = Post.get_by_id(id)
    if not post:
        return 'Postagem não encontrada', 404
    post = post.like()
    if not post:
        return 'Erro curtir postagem', 500
    return 'Postagem curtida com sucesso!', 200