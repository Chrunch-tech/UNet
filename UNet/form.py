from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import EmailField


class Search(FlaskForm):
    search = StringField("", validators=[DataRequired(), Length(max=100)])


class Login(FlaskForm):
    email = EmailField("Email: ", validators=[DataRequired(), Length(max=50)])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=8)])
    sign_in = SubmitField("Sign in")


class RegistrationForm(FlaskForm):
    first_name = StringField("First name: ", validators=[DataRequired(), Length(max=20)])
    last_name = StringField("Last name: ", validators=[DataRequired(), Length(max=15)])
    email = EmailField("Email: ", validators=[DataRequired(), Length(max=50)])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=8)])
    conform_password = PasswordField("Conform password: ", validators=[DataRequired(), Length(min=8)])
    register = SubmitField("Register")
