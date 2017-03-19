Information for TAs.
===

- Please make sure that the models created can be seeded using
  `seed.py`. (Get the students to use the same model in this
  repo)

- SQLAlchemy
    - Inheriting from `db.Model`, again.
    - Accessing information for specific `<rollno>`/`<code>`
      should get them familiar with `filter_by`.
    - The search features are supposed to introduce them to wildcards.

- `join` can be demostrated using the last two functionalities in the routes.
    - Ask to display course name/student name instead of course code and roll number.
      One way to do this is a join.

- The glue code to interface the modules together are split as follows:
    - Blueprint in `<module>/controllers.py`.
    - Integrated to larger app in `app/__init__.py`.
        - This reads configuration from `config.py`.


# Routes Required

```
/students/ - GET(read)
/students/<rollno> - GET(read), POST(update)
/students/create - GET(form), POST(create)
/students/<rollno>/delete - POST(delete)

/courses/ - GET(read)
/courses/<code> - GET(read), POST(update)
/courses/create - GET(form), POST(create)
/courses/<code>/delete - POST(delete)

-- Search. 
/students/search - GET
/courses/search - GET

/report/student/<rollno> - GET(read)
/report/course/<code> - GET(read)
/report/entry/<rollno>/<code> - GET(read)
```

## A little detail

`form` implies a basic form, so that CREATE can be demoed. The form posts to
the same link, which validates(?) the data and saves it into the database.

