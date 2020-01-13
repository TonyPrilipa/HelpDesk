from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TicketCreateForm(Form):

    header = StringField('Заголовок', validators=[DataRequired()])
    unit = SelectField('Отдел', choices=[('sysadmin', 'sysadmin'), ('Electro', 'electro')], validators=[DataRequired()])  #tuple 1 arg - returned data, 2 arg
    description = TextAreaField('Описание', validators=[DataRequired()])
    submit = SubmitField('Создать')