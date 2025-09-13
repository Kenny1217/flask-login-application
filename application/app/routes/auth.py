from flask import Blueprint, render_template, request
from ..forms.auth_forms import SignUpForm

auth_blueprint = Blueprint('auth', __name__, url_prefix = '/auth')

@auth_blueprint.route('/signup', methods = ['GET', 'POST'])
def signup():
    signup_form = SignUpForm()
    if request.method == 'POST':
        username = ""
        email = ""
        password = ""
        confirm_password = ""
    return render_template('./auth/signup.html', form = signup_form)

@auth_blueprint.route('/signin', methods = ['GET', 'POST'])
def signin():
    return render_template('./auth/signin.html')

@auth_blueprint.route('/signout', methods = ['GET', 'POST'])
def signout():
    return render_template('./auth/signout.html')

@auth_blueprint.route('/forgotpassword', methods = ['GET', 'POST'])
def forgotpassword():
    return render_template('./auth/forgotpassword.html')
