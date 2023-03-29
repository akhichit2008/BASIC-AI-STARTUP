from flask import Flask,render_template,request,url_for,redirect
import os
from Startup.models import *

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    basedirectory = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///'+os.path.join(basedirectory,'main_db.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app) #Add this line Before migrate line
    #migrate = Migrate(app, db)
    @app.route('/home')
    def home():
        return render_template('main.html') 
    @app.route('/login')
    def login():
        return "Hello Everybody"

    return app

if __name__ == "__main__":
    app = create_app()
