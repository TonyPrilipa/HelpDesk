from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_required, current_user
from .form import TicketCreateForm, TicketEditForm, FunctionalForm
from models import Ticket, Unit
from app import db
from flask_login import login_required

tickets = Blueprint('tickets', __name__, template_folder='templates')


@tickets.route('/', methods=['GET', 'POST'])
@login_required
def index():
    # in default tickets sorting by created date descending
    #FIXME need to filter function 
    order_method = Ticket.created.desc()
    if request.form.get('newest', False):
        order_method = Ticket.created.desc()
    if request.form.get('older', False):
        order_method = Ticket.created.asc()
        print(Ticket.in_work.desc())
    if request.form.get('by_status', False):
        order_method = Ticket.in_work.asc()
    tickets_list = Ticket.query.order_by(order_method).all()

    # show just user.unit tickets
    if request.form.get('user_unit', False):
        user_unit = Unit.query.filter_by(name=current_user.unit.name).first()
        tickets_list = Ticket.query.filter_by(unit=user_unit).all()
    return render_template('tickets/index.html', tickets_list=tickets_list, count=len(tickets_list))


@tickets.route('/<slug>', methods=['POST', 'GET'])
@login_required
def ticket_item(slug):
    ticket = Ticket.query.filter_by(slug=slug).first()
    func_form = FunctionalForm()
    if request.form.get('assign', False):
        ticket.in_work_by_user = current_user.username
        ticket.in_work = '1'
        db.session.add(ticket)
        db.session.commit()
    if request.form.get('done', False):
        ticket.in_work = '2'
        db.session.add(ticket)
        db.session.commit()
        return redirect(url_for('users.cabinet', username=current_user.username))
    return render_template('tickets/ticket.html', ticket=ticket, form=func_form)


@tickets.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = TicketCreateForm()

    if form.validate_on_submit():
        header = form.header.data
        unit = Unit.query.filter_by(name=form.unit.data).first()
        description = form.description.data
        check_task = Ticket.query.filter_by(name=header).first()
        if check_task is None:
            ticket = Ticket(name=header, 
                            unit=unit, 
                            description=description, 
                            who_create=current_user.username,
                            in_work='0')
            db.create_all()
            db.session.add(ticket)
            db.session.commit()
            return redirect(url_for('tickets.index'))
    return render_template('tickets/create.html', form=form)


@tickets.route('/<slug>/edit', methods=['POST', 'GET'])
@login_required
def edit_ticket(slug):
    form = TicketEditForm()
    ticket = Ticket.query.filter_by(slug=slug).first()
    if form.validate_on_submit():
        ticket.name = form.header.data
        ticket.unit = Unit.query.filter_by(name=form.unit.data).first()
        ticket.description = form.description.data
        db.session.add(ticket)
        db.session.commit()
        return redirect(url_for('tickets.ticket_item', slug=slug))
    elif request.method == 'GET':
        form.header.data = ticket.name
        form.unit.data = ticket.unit
        form.description.data = ticket.description
    return render_template('tickets/edit.html', form=form)



