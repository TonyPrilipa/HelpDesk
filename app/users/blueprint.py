from flask import Blueprint, render_template
from models import User
users = Blueprint('users', __name__, template_folder='templates')


@users.route('/')
def index():
    users = User.query.all()
    return render_template('users/index.html', users=users)

