from flask import Flask,render_template,request,url_for,redirect
from Startup.models import *


def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    '''app.config.from_mapping(
        SECRET_KEY='dev2023',
    )'''
    if test_config is None:
        app.config.from_pyfile('app_config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/home')
    def home():
        return render_template('main.html') 
    @app.route('/login')
    def login():
        return "Hello Everybody"

    return app
