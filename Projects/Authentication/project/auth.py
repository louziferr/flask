# project/auth.py
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import Login, User

auth = Blueprint('auth', __name__)

LoginDB = Login("login.db")

@auth.route('/login')
def login():
    return render_template('login.html', current_user=current_user)

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    login_success = LoginDB.login(email, password)

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not login_success:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    
    user = User(email, password)
    login_user(user, remember=remember)

    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html', current_user=current_user)

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = LoginDB.new_user(email, password, name)

    if not new_user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
