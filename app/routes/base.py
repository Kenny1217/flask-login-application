from flask import Blueprint, render_template

base_blueprint = Blueprint('/', __name__)

@base_blueprint.route('/')
def index():
    return render_template('./index.html')