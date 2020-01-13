from app import db
import re
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


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


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __repr__(self):
        return '<Id: {}, username: {}'.format(self.id, self.username)


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)

    role = db.relationship('User', backref='role ', lazy='dynamic')

    def __repr__(self):
        return '<Id: {}, role: {}'.format(self.id, self.name)

