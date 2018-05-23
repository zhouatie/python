# coding: utf8
from flask import Blueprint, render_template, request

admin = Blueprint('admin', __name__)


@admin.route('/login')
def login():
    return render_template('login.html')

@admin.route('/submit', methods=['post'])
def submit():
    print(request.form)
    return 'success'

