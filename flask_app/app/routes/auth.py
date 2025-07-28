from flask import Blueprint, render_template, request
from ..forms.auth_forms import SignupForm, LoginForm, ForgotPasswordForm

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignupForm()
    if request.method == 'POST':
        username = signup_form.username.data
        email = signup_form.email.data
        password = signup_form.password.data
        confirm_password = signup_form.confirm_password.data

    return render_template('./auth/signup.html', form=signup_form)

@auth_blueprint.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        username = login_form.username.data
        password = login_form.password.data

    return render_template('./auth/login.html', form=login_form)

@auth_blueprint.route('/forgotpassword', methods=['GET','POST'])
def forgotpassword():
    forgotpassword_form = ForgotPasswordForm()
    if request.method == 'POST':
        email = forgotpassword_form.email.data

    return render_template('./auth/forgotpassword.html', form=forgotpassword_form)
