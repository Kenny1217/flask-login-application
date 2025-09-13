from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo

class SignUpForm(FlaskForm):
    username = StringField('Username', validators = [InputRequired()])
    email = EmailField('Email', validators = [InputRequired(), Email()])
    password = StringField('Password', validators = [InputRequired()])
    confirm_password = StringField('Retype Password', validators = [InputRequired(), EqualTo('password')])
    submit = SubmitField('SignUp')
