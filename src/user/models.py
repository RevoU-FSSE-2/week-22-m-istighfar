from enum import Enum
from db import db
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import DateTime

class UserRole(Enum):
    ADMIN = 'admin'
    USER = 'user'

class User(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255))  
    role = db.Column(SqlEnum(UserRole), default=UserRole.USER, nullable=False)
    reset_password_token = db.Column(db.String(255), nullable=True)  
    reset_password_expires = db.Column(DateTime, nullable=True) 
    verified = db.Column(db.Boolean, default=False)  
    verification_token = db.Column(db.String(255), nullable=True) 
