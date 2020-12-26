""" Defining all the routes and apps used in this website """
from . import app
from .form import Search, Login, RegistrationForm
from flask import render_template, session, url_for, redirect
import os


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


@app.route('/', methods=["GET", "POST"])
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
        return redirect(url_for('login'))
    return render_template('register.html', register_form=register_form)
