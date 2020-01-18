from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired
from app import available_units


class TicketCreateForm(Form):

    header = StringField('Head', validators=[DataRequired()])
    unit = SelectField('Choice unit', choices=available_units(), validators=[DataRequired()])  #tuple 1 arg - returned data, 2 arg
    description = TextAreaField('What happened?', validators=[DataRequired()])
    submit = SubmitField('Create')


class FunctionalForm(Form):
    delete = SubmitField('Delete')
    confirm = SubmitField('Confirm')
