from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Retype Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Signup')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class ForgotPasswordForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()])
    submit = SubmitField('Reset Password')