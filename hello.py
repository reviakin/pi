# FLASK_APP=hello.py flask run
# FLASK_APP=hello.py FLASK_ENV=development flask run


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    name = "dima"
    return render_template('index.html', name=name)


@app.route('/french')
def bonjour_world():
    return 'bonjour world'


@app.route('/name/<name>')
def hello_name(name):
    return f"hello {name} "
