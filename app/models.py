from run import db
import enum
import bcrypt
from flask_login import UserMixin

class RoleEnum(enum.Enum):
    ADMIN = 'admin'
    SALESMAN = 'salesman'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum(RoleEnum), default=RoleEnum.SALESMAN, nullable=False)
    customers = db.relationship('Customer', backref='salesman', lazy=True)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def __repr__(self):
        return f'<User {self.username}>'

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cust_id = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(6), nullable=True)
    address = db.Column(db.String(500), nullable=True)
    payment_mode = db.Column(db.String(10), nullable=True)
    value = db.Column(db.String(10), nullable=True)
    sales_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Customer {self.name}>'

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cust_id = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    cust_type = db.Column(db.String(50), nullable=False)
    phone_no = db.Column(db.String(10), nullable=False)
    next_meeting = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f'<Lead {self.name}>'