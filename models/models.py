from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


Db = SQLAlchemy()


class User(Db.Model):
    __tablename__ = 'users'
    uid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    username = Db.Column(Db.String(64), unique=True, nullable=False)
    password = Db.Column(Db.String(128), nullable=False)


class Post(Db.Model):
    __tablename__ = 'posts'
    pid = Db.Column(Db.Integer, primary_key=True, autoincrement=True)
    author = Db.Column(Db.Integer, Db.ForeignKey('users.uid'), nullable=False)
    authorObj = Db.relation(User, backref='posts')
    content = Db.Column(Db.String(1024), nullable=False)
    createtime = Db.Column(Db.DateTime(timezone=False), nullable=False, default=datetime.utcnow)
