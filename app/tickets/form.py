from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired
from app import available_units


class TicketCreateForm(FlaskForm):

    header = StringField('Head', validators=[DataRequired()])
    unit = SelectField('Choice unit', choices=available_units(), validators=[DataRequired()])  #tuple 1 arg - returned data, 2 arg
    description = TextAreaField('What happened?', validators=[DataRequired()])
    submit = SubmitField('Create')


class FunctionalForm(FlaskForm):
    delete = SubmitField('Delete')
    confirm = SubmitField('Confirm')


class TicketEditForm(FlaskForm):
    header = StringField('Header', validators=[DataRequired()])
    unit = SelectField('Choice unit', choices=available_units(), validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Edit ticket')
