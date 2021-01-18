""" Defining all the routes and apps used in this website """
from . import app, bcrypt, db
from .db_model import Users, UserContent
from .form import Search, Login, RegistrationForm
from flask import render_template, session, url_for, redirect, flash
import os
import secrets


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/')
def home():
    """
    Defining the backend of home page
    :return: Home page 
    """
    return render_template("home.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    """
    Defining the backend of login page.
    :return: Login page
    """
    login_form = Login()
    if login_form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('login.html', login_form=login_form)


@app.route('/register', methods=["GET", "POST"])
def register():
    """
    Defining the backend of register page.
    :return: Register page
    """
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        first_name = register_form.first_name.data
        last_name = register_form.last_name.data
        email = register_form.email.data
        password = register_form.password.data
        comform_password = register_form.conform_password.data
        if password == comform_password:
            while True:
                user_id = secrets.token_hex(50)
                if comform_password == password:
                    if len(password) >= 8:
                        user = Users(id=str(user_id), first_name=first_name,
                            last_name=last_name, email=email,
                            password=bcrypt.generate_password_hash(password).decode("utf-8"))
                        db.session.add(user)
                        db.session.commit()
                        flash('Your account is successfully created! Now you\'ll able to login')
                        return redirect(url_for('login'))
                    else:
                        flash("The lenght of your password should be greater than or equal to 8")
                        return redirect(url_for('register'))
                else:
                    flash("Password dosen't match")
                    return redirect(url_for('register'))
        else:
            flash('Password dose\'nt match')
            return redirect(url_for('register'))
    return render_template('register.html', register_form=register_form)


@app.route('/profile', methods=["GET", "POST"])
def profile():
    search = Search()
    if search.validate_on_submit():
        return redirect(url_for('profile'))
    return render_template('profile.html', search=search)
