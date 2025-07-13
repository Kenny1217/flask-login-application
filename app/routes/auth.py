from flask import Blueprint, render_template

auth_blueprint = Blueprint('/auth', __name__)

@auth_blueprint.route('/auth/signup', methods=['GET', 'POST'])
def signup():
    return render_template('./auth/signup.html')

@auth_blueprint.route('/auth/signin', methods=['GET', 'POST'])
def signin():
    return render_template('./auth/signin.html')

@auth_blueprint.route('/auth/logout', methods=['GET', 'POST'])
def logout():
    return render_template('./auth/logout.html')

@auth_blueprint.route('/auth/forgotpassword', methods=['GET', 'POST'])
def forgotPassword():
    return render_template('./auth/forgotpassword.html')
