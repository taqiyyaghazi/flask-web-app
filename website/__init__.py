from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'qwertyuiop' #Inisiasi secret key -> Secret key bebas

    return app