from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class EditProfileForm(FlaskForm):

    real_name = StringField('Real name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    about = TextAreaField('About', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])
