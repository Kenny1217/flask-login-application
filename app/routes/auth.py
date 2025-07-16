from flask import Blueprint, render_template, request, redirect, url_for
import bcrypt

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
    return render_template('./auth/signup.html')

@auth_blueprint.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Get users password hash
        stored_password = ""

        stored_password_bytes = stored_password.encode('utf-8')
        password_bytes = password.encode('utf-8')

        if bcrypt.checkpw(password_bytes, stored_password_bytes):
            print('User {username} has authenticated')
            return redirect(url_for(''))
        else:
            print('User {username} has not authenticated')
            return render_template('./auth/signin.html')
    return render_template('./auth/signin.html')

@auth_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('./auth/logout.html')

@auth_blueprint.route('/forgotpassword', methods=['GET', 'POST'])
def forgotPassword():
    if request.method == 'POST':
        email = request.form.get('email')
    return render_template('./auth/forgotpassword.html')
