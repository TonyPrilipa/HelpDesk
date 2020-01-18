from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_required, current_user
from .form import TicketCreateForm, FunctionalForm
from models import Ticket, Unit
from app import db
from flask_login import login_required

tickets = Blueprint('tickets', __name__, template_folder='templates')


@tickets.route('/')
@login_required
def index():
    tickets = Ticket.query.all()
    return render_template('tickets/index.html', tickets_list=tickets)


@tickets.route('/<slug>', methods=['POST', 'GET'])
def ticket_item(slug):
    ticket = Ticket.query.filter_by(slug=slug).first()
    func_form = FunctionalForm()
    if request.form:
        if request.form['delete']:
            db.session.delete(ticket)
            db.session.commit()
            return redirect(url_for('tickets.index'))
    return render_template('tickets/ticket_item.html', ticket=ticket, form=func_form)


@tickets.route('/create', methods=['GET', 'POST'])
def create():
    form = TicketCreateForm()
    if form.validate_on_submit():
        header = form.header.data
        unit = Unit.query.filter_by(name=form.unit.data).first()
        description = form.description.data
        ticket = Ticket(name=header, unit=unit, description=description, who_create=current_user.username)
        db.create_all()
        db.session.add(ticket)
        db.session.commit()

        return redirect(url_for('tickets.index'))
    return render_template('tickets/create.html', form=form)
