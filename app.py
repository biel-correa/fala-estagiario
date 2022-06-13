from flask import Flask

app = Flask(__name__)

from controller import HomeController
from controller import PostController

if __name__ == '__main__':
    app.run()