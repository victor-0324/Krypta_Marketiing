from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
# from flask_login import login_user, logout_user, current_user, login_required
# from werkzeug.security import check_password_hash
# from src.database.querys import Querys 

initial_app = Blueprint("initial_app", __name__, url_prefix="/")

@initial_app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('pages/index.html')
 