from flask import Flask, request, render_template

app = Flask(__name__)
users = dict()


@app.route('/', methods=['GET'])
def home():
    return render_template('home_page.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return 'Pagina Sendo Criada'
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        request.jsonify()
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)