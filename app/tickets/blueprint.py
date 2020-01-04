from flask import Blueprint, render_template, url_for
from models import Ticket

tickets = Blueprint('tickets', __name__, template_folder='templates')



@tickets.route('/')
def index():
    tickets = Ticket.query.all()
    return render_template('tickets/index.html', tickets_list=tickets)

@tickets.route('/<slug>')
def ticket_item(slug):
    ticket = Ticket.query.filter_by(slug=slug).first()
    return render_template('tickets/ticket_item.html', ticket=ticket)