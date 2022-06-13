from flask import Flask

app = Flask(__name__)

from controller import HomeController

if __name__ == '__main__':
    app.run()