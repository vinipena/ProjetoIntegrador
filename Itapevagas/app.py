from flask import Flask, app, render_template

app = Flask('__name__')

@app.route('/')
def index():
    return render_template(index.html)