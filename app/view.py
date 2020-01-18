from app import app
from flask import render_template, session

@app.route('/')
def index():
    return render_template('index.html', session=session)
