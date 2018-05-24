# coding: utf8
from blogs import app
from flask_sqlalchemy import SQLAlchemy
import pymysql
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://qdm175040417:843175489@115.28.182.199:3306/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    account = db.Column(db.String(100))
    password = db.Column(db.String(100))
