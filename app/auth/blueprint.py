from flask import Blueprint, render_template, redirect, request, flash, url_for
from .form import LoginForm, RegistrationForm
from models import User, Unit
from flask_login import login_user, logout_user, login_required
from app import db

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('index'))
        flash('Invalid username')
    return render_template('auth/index.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        unit = Unit.query.filter_by(name=form.unit.data).first()
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data,
                    phone=form.phone.data,
                    real_name=form.real_name.data,
                    unit=unit)
        db.session.add(user)
        db.session.commit()
        flash('You can now login')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
