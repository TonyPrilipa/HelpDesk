from app import app
from flask import render_template, session, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('tickets.index'))
    #return render_template('index.html', session=session)
