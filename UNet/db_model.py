from . import db
import datetime


class Users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String(50), primary_key=True, unique=True)
    user_content = db.relationship('userContent', backref="users")
    first_name = db.Column(db.String(20), nullable=False, unique=True)
    last_name = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    friends = db.Column(db.String(50), nullable=True, unique=False)
    following = db.Column(db.String(50), nullable=True, unique=False)
    followers = db.Column(db.Integer, nullable=False, unique=False)
    password =  db.Column(db.String(1000), nullable=False, unique=False)
    profile_img = db.Column(db.String(60), nullable=True, unique=False)
    about = db.Column(db.Text, nullable=True, unique=False)

    def __repr__(self):
        return f"<User>[first_name: {self.first_name}, last_name: {self.last_name}]"

class UserContent(db.Model):
    __tablename__ = "userContent"
    user_id = db.Column(db.String(50), db.ForeignKey('users.user_id'), primary_key=True)
    shared_images = db.Column(db.String(25), nullable=True, unique=True)
    videos = db.Column(db.String(25), nullable=True, unique=True)
    posts = db.Column(db.Text, nullable=True, unique=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def  __repr__(self):
        return f"<User_content>[shared_images: {self.shared_images}, videos: {self.videos}, posts: {self.posts}, date_time: {self.date_time}]"
