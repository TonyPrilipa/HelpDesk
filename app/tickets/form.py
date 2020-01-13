from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

def available_units():
    from models import Unit
    names = []
    units = Unit.query.with_entities(Unit.name).all()
    for unit in units:
        unit_tuple = unit.name, unit.name
        names.append(unit_tuple)
    return names


class TicketCreateForm(Form):

    header = StringField('Заголовок', validators=[DataRequired()])
    unit = SelectField('Отдел', choices=available_units(), validators=[DataRequired()])  #tuple 1 arg - returned data, 2 arg
    description = TextAreaField('Описание', validators=[DataRequired()])
    submit = SubmitField('Создать')
