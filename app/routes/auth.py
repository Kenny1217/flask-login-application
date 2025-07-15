from flask import Blueprint, render_template, request

auth_blueprint = Blueprint('/auth', __name__)

@auth_blueprint.route('/auth/signup', methods=['GET', 'POST'])
def signup():
    return render_template('./auth/signup.html')

@auth_blueprint.route('/auth/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
    return render_template('./auth/signin.html')

@auth_blueprint.route('/auth/logout', methods=['GET', 'POST'])
def logout():
    return render_template('./auth/logout.html')

@auth_blueprint.route('/auth/forgotpassword', methods=['GET', 'POST'])
def forgotPassword():
    if request.method == 'POST':
        email = request.values.get('email')
    return render_template('./auth/forgotpassword.html')
