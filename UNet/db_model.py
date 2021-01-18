from . import db
import datetime


class Users(db.Model):
    id = db.Column(db.String(50), primary_key=True, unique=True)
    first_name = db.Column(db.String(20), nullable=False, unique=True)
    last_name = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    friends = db.Column(db.String(50), nullable=True, unique=False)
    following = db.Column(db.String(50), nullable=True, unique=False)
    followers = db.Column(db.String(50), nullable=True, unique=False)
    password =  db.Column(db.String(1000), nullable=False, unique=False)
    profile_img = db.Column(db.String(60), unique=True, default="static/default.svg")
    about = db.Column(db.Text, nullable=True, unique=False)
    user_content = db.relationship('UserContent', backref="users", lazy=True)

    def __repr__(self):
        return f"<User>[first_name: {self.first_name}, last_name: {self.last_name}]"

class UserContent(db.Model):
    __tablename__ = "user_content" 
    id = db.Column(db.String(50), db.ForeignKey('users.id'), primary_key=True)
    content_id = db.Column(db.String(50), nullable=False, unique=True)
    shared_images = db.Column(db.String(25), nullable=True, unique=True)
    videos = db.Column(db.String(25), nullable=True, unique=True)
    posts = db.Column(db.Text, nullable=True, unique=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    daily_status = db.relationship("DailyStatus", backref="usercontent", lazy=True)
    likes = db.Column(db.Integer, nullable=True, unique=False)
    loves = db.Column(db.Integer, nullable=True, unique=False)
    comment = db.Column(db.Text, nullable=True, unique=False)
    response = db.Column(db.Text, nullable=True, unique=False)

    def  __repr__(self):
        return f"<User_content>[shared_images: {self.shared_images}, videos: {self.videos}, posts: {self.posts}, date_time: {self.date_time}]"

class DailyStatus(db.Model):
    id = db.Column(db.String(50), db.ForeignKey('user_content.id'), primary_key=True)
    status_id = db.Column(db.String(50), nullable=False, unique=True)
    title = db.Column(db.String(100), nullable=False, unique=False)
    images = db.Column(db.Text, nullable=True, unique=True)
    videos = db.Column(db.Text, nullable=True, unique=True)
    text = db.Column(db.Text, nullable=True, unique=False)
    comment = db.Column(db.Text, nullable=True, unique=False)
    response = db.Column(db.Text, nullable=True, unique=False)

    def __repr__(self):
        return f"<DailyStatus>[assent: [{self.images}, {self.videos}, {self.text}], title: {self.title}]"

class Requests(db.Model):
    _from = db.Column(db.String(50), primary_key=True)
    _to = db.Column(db.String(50), nullable=False, unique=False)
    status = db.Column(db.Integer, nullable=False, unique=False)

    def __repr__(self):
        return f"<Requests>[from: {self._form}, to: {self._to}]"
