from app import db


class Poem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    text = db.Column(db.String(1028), unique=True)


class Humoresque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    text = db.Column(db.String(1028), unique=True)