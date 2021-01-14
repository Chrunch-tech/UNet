from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import secrets


app = Flask(__name__)
SECRET_KEY = secrets.token_hex(50)
app.config['SECRET_KEY'] = str(SECRET_KEY)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UNet.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from . import route
from . import db_model
