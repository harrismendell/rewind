# import flask class and a render_template
from flask import Flask, render_template, request, redirect


# Create new instance of flask class
app = Flask(__name__)


@app.route('/')
def title_screen():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)