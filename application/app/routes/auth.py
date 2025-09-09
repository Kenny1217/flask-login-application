from flask import Blueprint, render_template

auth_blueprint = Blueprint('auth', __name__, url_prefix = '/auth')

@auth_blueprint.route('/signup', methods = ['GET', 'POST'])
def signup():
    return render_template('./auth/signup.html')

@auth_blueprint.route('/signin', methods = ['GET', 'POST'])
def signin():
    return render_template('./auth/signin.html')
