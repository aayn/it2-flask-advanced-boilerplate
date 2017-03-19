from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.courses.models import Course

mod_courses = Blueprint('courses', __name__, url_prefix='/courses')

@mod_courses.route('/', methods=['GET'])
def get_all_courses():
    courses = Course.query.all()
    return render_template('courses/index.html', courses=courses)

@mod_courses.route('/search', methods=['GET'])
def search_courses():
    qstr = request.args.get('q')
    sqlqstr = '%%%s%%'%(qstr)
    courses = Course.query.filter(Course.name.like(sqlqstr)).all()
    return render_template('courses/index.html', courses=courses)

@mod_courses.route('/<code>', methods=['GET'])
def get_student(code):
    course = Course.query.filter(Course.code == code).all()
    return render_template('courses/index.html', courses=course)

