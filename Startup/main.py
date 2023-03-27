from Startup import create_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os

basedirectory = os.path.abspath(os.path.dirname(__file__))

app = create_app()

app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///'+os.path.join(basedirectory,'main_db.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
