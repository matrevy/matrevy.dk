.. highlight:: bash

==========
matrevy.dk
==========

This repository contains the source code for the Matematikrevy website at
`matrevy.dk`_.

.. _`matrevy.dk`: https://matrevy.dk/

Getting started
---------------

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

Prerequisites
^^^^^^^^^^^^^

* Python_ (>= 3.6)
* PostgreSQL_ (>= 9.5)
* Git_

.. _Python: https://www.python.org/
.. _PostgreSQL: https://www.postgresql.org/
.. _Git: https://git-scm.com/

Installation
^^^^^^^^^^^^

1.  Clone this repository and go into the directory ::

        git clone https://github.com/matrevy/matrevy.dk.git
        cd matrevy.dk

2.  Create a virtual environment ::

        python3 -m venv env

3.  Activate the virtual environment

    **On macOS/Linux:** ::

        source env/bin/activate

    **On Windows:** ::

        .\env\Scripts\activate

4.  Install dependencies ::

        pip install -r requirements/dev.txt

5.  Create the file ``config/secrets.json`` with the following content

    .. code:: json

        {
          "FILENAME": "secrets.json",
          "SECRET_KEY": "<random string>",
          "DB_NAME": "matrevy_db",
          "DB_USER": "matrevy",
          "DB_PASSWORD": "<database password>",
          "DB_HOST": "localhost",
          "DB_PORT": "5432"
        }

    Replace the values for ``SECRET_KEY`` and ``DB_PASSWORD`` with a long
    random string and your database password respectively.

Database setup
^^^^^^^^^^^^^^

6.  Connect to PostgreSQL ::

        psql -U postgres

7.  Create database

    .. code:: sql

        CREATE USER matrevy SUPERUSER PASSWORD '<database password>';
        CREATE DATABASE matrevy_db WITH OWNER matrevy;
        \q

8.  Run migrations ::

        python manage.py migrate

9.  Create admin user ::

        python manage.py createsuperuser

Usage
^^^^^

10. Compile Sass to CSS ::

        pysassc scss/main.scss static/css/main.css

11. Start development server ::

        python manage.py runserver 0.0.0.0:8000

    The development site should now be available at http://localhost:8000.
    To access the admin panel, open http://localhost:8000/admin and log in
    using the admin user created earlier.

Contributing
------------

Found a bug or have a suggestion? Feel free to `create an issue`_ and/or make
a pull request!

In general, we follow the "fork-and-pull" Git workflow.

1. **Fork** the repo on GitHub
2. **Clone** the project to your own machine
3. **Commit** changes to your own branch
4. **Push** your work back up to your fork
5. Submit a **Pull request** so that we can review your changes

.. _`create an issue`: https://github.com/matrevy/matrevy.dk/issues/new

Built with
----------

* Django_ - The web framework used
* Bootstrap_ - CSS framework

.. _Django: https://www.djangoproject.com/
.. _Bootstrap: https://getbootstrap.com/

License
-------

This project is licensed under the terms of the MIT license.
See the LICENSE_ file for details.

.. _LICENSE: LICENSE
