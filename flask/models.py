# models.py
from app import db  # Correct import statement, not from 'flask.app'
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # "customer", "barber", or "admin"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Barber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    available_slots = db.Column(db.String(500))  # Simple string for now

    user = db.relationship("User", backref="barber", lazy=True)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barber_id = db.Column(db.Integer, db.ForeignKey("barber.id"))
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    date_time = db.Column(db.DateTime, nullable=False)

    barber = db.relationship("Barber", backref="appointments", lazy=True)
    customer = db.relationship("User", backref="appointments", lazy=True)


