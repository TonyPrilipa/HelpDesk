from flask import Blueprint, render_template, abort, redirect, url_for
from flask_login import current_user
from models import User
from .form import EditProfileForm
from app import db
users = Blueprint('users', __name__, template_folder='templates')


@users.route('/')
def index():
    users = User.query.all()
    return render_template('users/index.html', users=users)


@users.route('/<username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('users/user_profile.html', user=user)

@users.route('/edit-profile/<username>', methods=['GET', 'POST'])
def edit_profile(username):
    form = EditProfileForm()
    user = User.query.filter_by(username=username).first()
    if form.validate_on_submit():
        user.real_name = form.real_name.data
        user.phone = form.phone.data
        user.about = form.about.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.user_profile', username=username))
    user.real_name = form.real_name.data
    user.phone = form.phone.data
    user.about = form.about.data
    return render_template('users/edit_profile.html', form=form)
