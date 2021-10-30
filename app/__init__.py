from flask import Flask, request, render_template, redirect, url_for
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)
app.config['SECRET_KEY'] = 'secret'
