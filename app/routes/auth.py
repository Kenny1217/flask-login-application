from flask import Blueprint, render_template

auth_blueprint = Blueprint('/auth', __name__)

@auth_blueprint.route('/auth/forgotpassword', methods=['GET', 'POST'])
def forgotPassword():
    return render_template('./auth/forgotpassword.html')

@auth_blueprint.route('/auth/login', methods=['GET', 'POST'])
def login():
    return render_template('./auth/login.html')

@auth_blueprint.route('/auth/logout', methods=['GET', 'POST'])
def logout():
    return render_template('./auth/logout.html')

@auth_blueprint.route('/auth/register', methods=['GET', 'POST'])
def register():
    return render_template('./auth/register.html')