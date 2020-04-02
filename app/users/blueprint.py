from flask import Blueprint, render_template, abort, redirect, url_for, request
from flask_login import current_user
from models import User, Ticket, Unit
from .form import EditProfileForm
from app import db
from flask_login import login_required
users = Blueprint('users', __name__, template_folder='templates')


@users.route('/')
@login_required
def index():
    users = User.query.all()
    return render_template('users/index.html', users=users)


@users.route('/<username>', methods=['GET', 'POST'])
@login_required
def user_profile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('users/user_profile.html', user=user)


@users.route('/edit-profile/<username>', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
    form = EditProfileForm()
    user = User.query.filter_by(username=username).first()
    if form.validate_on_submit():
        user.real_name = form.real_name.data
        user.phone = form.phone.data
        user.about = form.about.data
        user.email = form.email.data
        user.unit = Unit.query.filter_by(name=form.unit.data).first()
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.cabinet', username=username))
    elif request.method == 'GET':
        form.real_name.data = user.real_name
        form.phone.data = (user.phone or 'None')
        form.about.data = (user.about or 'None')
        form.email.data = (user.email)
    return render_template('users/edit_profile.html', form=form)


@login_required
@users.route('/cabinet/<username>')
def cabinet(username):
    if username != current_user.username:
        abort(403)
    ticket_list = Ticket.query.filter_by(in_work_by_user=current_user.username).all()
    return render_template('users/cabinet.html', username=username, ticket_list=ticket_list)