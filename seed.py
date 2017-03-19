from flask_sqlalchemy import SQLAlchemy
import flask
import os

app = flask.Flask(__name__)
app.config['DEBUG'] = True
base_dir = os.path.abspath(os.path.dirname(__file__))  
sqlalchemy_database_uri = 'sqlite:///' + os.path.join(base_dir, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_database_uri
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    rollno = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, roll, name):
        self.rollno = roll
        self.name = name

    def __repr__(self):
        return "Student { name: %r, rollno: %r }"%(self.rollno, self.name)


class Course(db.Model):
    __tablename__= 'course'
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    code = db.Column(db.String(10), primary_key=True)

    def __init__(self, code, name, description):
        self.code = code
        self.name = name
        self.description = description

    def __repr__(self):
        return "Course { code: %r, name: %r, description: %r}"%(self.code, 
                self.name, self.description)


class GradeEntry(db.Model):
    __tablename__ = 'grade_entry'
    assignments = db.Column(db.Float)
    labs = db.Column(db.Float)
    mids = db.Column(db.Float)
    end_sem = db.Column(db.Float)
    student_roll = db.Column(db.String(8), db.ForeignKey("student.rollno"))
    course_code = db.Column(db.String(10), db.ForeignKey("course.code"))
    id = db.Column(db.Integer, primary_key=True)


    def __init__(self, r):
        self.assignments = 0.0
        self.labs = 0.0
        self.mids = 0.0
        self.end_sem = 0.0

    def set(self, **kwargs):
        if "assignments" in kwargs:
            self.assignments = kwargs["assignments"]

        if "labs" in kwargs:
            self.labs = kwargs["labs"]

        if "mids" in kwargs:
            self.mids = kwargs["mids"]

        if "end_sem" in kwargs:
            self.end_sem = kwargs["end_sem"]

db.create_all()

db.session.add(Student('201401071', 'Jerin Philip'))
db.session.add(Student('201401065', 'Vishal Kaja'))
db.session.add(Course( 'ICS102', 'IT Workshop II',''))
db.session.add(Course( 'IEC101', 'Basic Electronic Circuits',''))
db.session.commit()

