from app import db
import re
from datetime import datetime

def slugify(name):
    pattern = r'[^\w+]'.lower()
    slug = re.sub(pattern, '-', name)
    return slug.lower()

class Ticket(db.Model):

    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(140))
    slug = db.Column(db.String(40), unique=True)
    created = db.Column(db.DateTime, default=datetime.now())
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'))

    def __init__(self, *args, **kwargs):
        super(Ticket, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def __repr__(self):
        return '<Id: {0}, Name: {1}, slug: {2}>'.format(self.id, self.name, self.slug)


class Unit(db.Model):
    __tablename__ = 'units'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)

    ticket = db.relationship('Ticket', backref='unit', lazy='dynamic')

    def __repr__(self):
        return '<Id: {0}, Name: {1}>'.format(self.id, self.name)