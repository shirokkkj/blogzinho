from flask import Blueprint, render_template

navbar = Blueprint('nav', __name__)

@navbar.route('/nav')
def nav():
    return render_template('navbar.html')