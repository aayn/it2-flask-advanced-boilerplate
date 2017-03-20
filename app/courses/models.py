from flask_sqlalchemy import SQLAlchemy
from app import db

class Course(db.Model):
    __tablename__= 'course'
    # Define the fields here

    def __init__(self, code, name, description):
        # Fill this up

    def __repr__(self):
        return "Course { code: %r, name: %r, description: %r}"%(self.code,
                self.name, self.description)
