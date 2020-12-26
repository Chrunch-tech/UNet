from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "Y6SfnP5cwFGi42s9T3IKKxDn3XY5vDGdjQN-b1IRdSo"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UNet.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from . import route
