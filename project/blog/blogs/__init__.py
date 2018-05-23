from flask import Flask
from blogs.home import home
from blogs.admin import admin

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(admin, url_prefix='/admin')


