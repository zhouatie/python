# coding: utf8
from flask import Blueprint, render_template

home = Blueprint('home', __name__)


@home.route('/')
def index():
    return '<div>hello</div>'

