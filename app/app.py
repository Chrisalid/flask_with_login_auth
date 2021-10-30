from flask import Flask, request, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user

app = Flask(__name__)
login_manager = LoginManager(app)