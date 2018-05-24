# coding: utf8
from flask import Blueprint, render_template, request
from blogs.models import db, User

admin = Blueprint('admin', __name__)


@admin.route('/login')
def login():
    return render_template('login.html')

@admin.route('/submit', methods=['post'])
def submit():
    # request.form['account']
    u = User(name='john', email='john@email.com')
    db.session.add(u)
    return 'success'

