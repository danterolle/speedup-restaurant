from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
db = SQLAlchemy(app)


class Reservation(db.Model):
    __tablename__ = "reservations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    num_people = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    notes = db.Column(db.String(200))

    def __init__(self, name, surname, email, phone, num_people, date, time, notes):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.num_people = num_people
        self.date = date
        self.time = time
        self.notes = notes

    def __repr__(self):
        return f'<Reservation {self.name} {self.surname}>'


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, nullable=False)
    items = db.Column(db.String(200), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, table_number, items, total_price):
        self.table_number = table_number
        self.items = items
        self.total_price = total_price

    def __repr__(self):
        return f'<Order {self.id}>'
