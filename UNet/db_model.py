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
    shared_images = db.Column(db.String(25), nullable=True, unique=True)
    videos = db.Column(db.String(25), nullable=True, unique=True)
    posts = db.Column(db.Text, nullable=True, unique=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    daily_status = db.relationship("DailyStatus", backref="usercontent", lazy= True)

    def  __repr__(self):
        return f"<User_content>[shared_images: {self.shared_images}, videos: {self.videos}, posts: {self.posts}, date_time: {self.date_time}]"

class DailyStatus(db.Model):
    id = db.Column(db.String(50), db.ForeignKey('users.id'), primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=False)
    assets = db.Column(db.String(200), nullable=True , unique=False)
    user_id = db.Column(db.String(50), db.ForeignKey('user_content.id'))

    def __repr__(self):
        return f"<DailyStatus>[assent: {self.assets}, title: {self.title}]"
