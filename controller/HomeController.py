from app import app
from flask import render_template

from model.Post import Post

@app.route('/', methods=['GET'])
def home():
    posts = Post.get_all()
    return render_template('home.html', posts=posts)