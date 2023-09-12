from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('base.html')

@app.route('/<number>')
def ksiega(number):
    number = int(number[1:])
    if(number>=1 or number<=12):
        return render_template(f'k{escape(number)}.html')
    return index()
