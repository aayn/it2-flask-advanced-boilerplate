from flask_sqlalchemy import SQLAlchemy
from app import db

class Student(db.Model):
    __tablename__ = 'student'
    # Define the fields here

    def __init__(self, roll, name):
        # fill this up

    def __repr__(self):
        return "Student { name: %r, rollno: %r }"%(self.rollno, self.name)
