from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email
from app import available_units


class EditProfileForm(FlaskForm):
    real_name = StringField('Real name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone')
    about = TextAreaField('About')
    unit = SelectField('Unit', choices=available_units(), validators=[DataRequired()])
    submit = SubmitField('Submit')