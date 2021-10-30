from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user
from app.models import Users
from app import app

@app.route('/')
def home():
    return render_template('home_page.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        pwd = request.form.get('password')

        if name and email and pwd:
            try:
                print('Passou')
                user = Users(name, email, pwd)
                user.save()

                return redirect(url_for('login'))
            except Exception:
                return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        pwd = request.form.get('password')

        user = Users.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)