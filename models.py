from app import db

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    start_time = db.Column(db.String(100))
    participants = db.Column(db.Text)
