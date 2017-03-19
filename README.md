Information for TAs.
===

- Please make sure that the models created can be seeded using =seed.py=. (Get
  the students to use the same model in this repo)

- The search features are supposed to introduce them to wildcards.

- `join` can be demostrated using the last two functionalities. 
    - Ask to display course name/student name instead of course code and roll number.
      One way to do this is a join.

- The glue code to interface the modules together are split as follows:
    - Blueprint in `<module>/controllers.py`.
    - Integrated to larger app in `app/__init__.py`.
        - This reads configuration from `config.py`.
