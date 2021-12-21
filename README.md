# Test project for learning Django

# Create project directory
`mkdir PROJECT_ROOT_NAME`
`cd PROJECT_ROOT_NAME`

# Create virtual env for dependencies, including Django
`pipenv install Django`

# Enter virtual env
`pipenv shell`

# Create new project in the current directory
`django-admin startproject PROJECT_NAME .`

# Create db migration script for the initial db structure and run it
`python manage.py makemigrations`
`python mange.py migrate`

# Create superuser for authentication/admin panel
`python manage.py createsuperuser`

# Start server
`python manage.py runserver 0.0.0.0:0000`

# Create app
`python manage.py startapp APP_NAME`
# Add APP_NAME to INSTALLED_APPS in the PROJECT_NAME/settings


# Create a Model
In APP_NAME/models.py create a new Model class:

    class MODEL_NAME(models.Model):
        text = models.CharField(max_lenght=140)


