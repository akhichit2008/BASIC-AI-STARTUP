from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(500),unique=True,nullable=False)
    email = db.Column(db.String(100),unique=True,nullable=False)
    creation = db.Column(db.DateTime(timezone=True),
    server_default=func.now())
    password = db.Column(db.String(80),nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

