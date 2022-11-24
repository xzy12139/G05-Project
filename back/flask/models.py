# 存储数据库模型
from exts import db
from sqlalchemy import ForeignKey

class UserModel(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.String(20), nullable=False, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

class Thesis(db.Model):
    __tablename__ = "thesis"
    thesis_id = db.Column(db.String(50), nullable=False, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    publication_date = db.Column(db.date)
    journal = db.Column(db.String(30), nullable=False)
    abstract = db.Column(db.String(900), nullable=False)
    link = db.Column(db.String(100))
    citation_num = db.Column(db.Int)
    rating = db.Column(db.Double)

class Favorites(db.Model):
    __tablename__ = "favorites"
    user_id = db.Column(db.String(20), ForeignKey('user.user_id'), nullable=False, primary_key=True)
    thesis_id = db.Column(db.String(20), ForeignKey('thesis.thesis_id'), nullable=False, primary_key=True)