from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Home Page!</h1>"


@app.route('/hello')
@app.route('/hello/<name>')
@app.route("/hello/<name>/<int:time_id>")
def hello(name=None, time_id=None):
    time = None
    if time_id is not None:
        time = str(time_id)
        if time_id % 10 == 1 and time_id % 100 != 11:
            time += "st"
        elif time_id % 10 == 2 and time_id % 100 != 12:
            time += "nd"
        else:
            time += "th"

    return render_template('hello.html', name=name, time=time)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run(debug=True)
