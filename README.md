1. Python 3.8
Description : This is the project which has been implemented using Django framework
with python libraries to populate JSON data based on the requirement provided on the email.

Prerequisite's
IDE : Pycharm

libraries:
- Faker
- Django
- Django REST framework

Database : Sqlite3

Summary: Django application for User and Activity Period models, implemented a custom management command to populate the database with some dummy data,
and designed an API to serve that data in the json format.

Project Description :

- Set up Django
- Create a model in the database that the Django ORM will manage
- Set up the Django REST Framework
- Serialize the model from step 2
- Create the URL endpoints to view the serialized data.


Set up Django
 - Virtual Environment
 - Install Django
 - Make project directory
 - Create App -> Django-admin startapp (app_name)
 - Run server to check your project is running or not -> python manage.py runserver
 - We have to migrate the Database -> python manage.py migrate
 - Next, make migrations.
 - Later we've to create Superuser by giving Name, email, Password.
 - To break server Press CRTL + C

Faker : Faker is the library to populate the dummy data to database. For this we've to install Faker, And create a new file to populate data.
Next, run the file -> python file_name.py
