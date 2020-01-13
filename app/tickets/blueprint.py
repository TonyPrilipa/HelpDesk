from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import login_required
from .form import TicketCreateForm
from models import Ticket, Unit
from app import db

tickets = Blueprint('tickets', __name__, template_folder='templates')



@tickets.route('/')
@login_required  #  не дает доступ не аутинтефицированым юзерам
def index():
    tickets = Ticket.query.all()
    return render_template('tickets/index.html', tickets_list=tickets)

@tickets.route('/<slug>')
def ticket_item(slug):
    ticket = Ticket.query.filter_by(slug=slug).first()
    return render_template('tickets/ticket_item.html', ticket=ticket)

@tickets.route('/create', methods=['GET', 'POST'])
def create():
    form = TicketCreateForm()
    if form.validate_on_submit():
        header = form.header.data
        unit = Unit.query.filter_by(name=form.unit.data).first()
        description = form.description.data
        ticket = Ticket(name=header, unit=unit, description=description)
        db.create_all()
        db.session.add(ticket)
        db.session.commit()

        return redirect(url_for('index'))


    return render_template('tickets/create.html', form=form)