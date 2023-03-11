# Ecommerce API using Django, Django REST Framework and MySQL

## Steps to get the project up and running

1. Make sure you have Python v3.10 installed on your machine to run this project without issues
2. Make virtual env to project using the following command
```
python3.10 -m venv env
```
3. Install project requirements using the following command
```
python -m pip install requirements.txt
```
4. Make your MySQL database and update database settings in settings.py file
```
{project_path}/app/settings.py
```
5. Migrate your database using the following command
```
python manage.py migrate
```
6. Create super user using the following command then enter your super user password (Make sure you remember this password)
```
python manage.py createsuperuser --email admin@ecommerce.django.com --username admin
```
