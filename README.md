# Test project for learning Django

### Create project directory
    mkdir PROJECT_ROOT_NAME
    cd PROJECT_ROOT_NAME

### Create virtual env for dependencies, including Django
    pipenv install Django

### Enter virtual env
    pipenv shell

### Create new project in the current directory
    django-admin startproject PROJECT_NAME .

### Create db migration script for the initial db structure and run it
    python manage.py makemigrations
    python mange.py migrate

### Create superuser for authentication/admin panel
    python manage.py createsuperuser

### Start server
    python manage.py runserver 0.0.0.0:0000

### Create app
    python manage.py startapp APP_NAME
    
    Add APP_NAME to INSTALLED_APPS in the PROJECT_NAME/settings

### Create a Model
In APP_NAME/models.py create a new Model class:

    class MODEL_NAME(models.Model):
        text = models.CharField(max_lenght=140)
        ...

Then, run makemigrations to create the db update script.
Run migrate to execute the update.
Register the model in the APP_NAME/admin.py

    from .models import MODEL_NAME

    class MODEL_NAMEAdmin(admin.ModelAdmin):
        pass

Then, in the same file, register the admin class and connect 
it to the model class

    admin.site.register(MODEL_NAME, MODEL_NAMEAdmin)

Add a `__str__(self)` method to the Model class for a better
string representation of the object in the admin panel

    def __str__(self):
        return some_text

### Adding a view (class based) to list our model objects

In APP_NAME/VIEWS.py create a new View class:

    from django.views.generic import ListView
    from .models import MODEL_NAME

    class HomePage(ListView):
        http_method_names = ["get"]
        template_name = "homepage.html"
        model = MODEL_NAME
        context_object_name = MODEL_NAME_PLURAL
        queryset = MODEL_NAME.objects.all().order_by('-id')[0:30]

Create a urls.py in APP_NAME/
Add a new urlpattern:

    from django.urls import path
    from . import views

    # used for namespacing
    app_name = APP_NAME

    urlpatterns = [path("", views.HomePage.as_view(), name="index.html")]

Include the new urlpatterns in PROJECT_NAME/urls.py

    from django.contrib import admin
    from django.urls import path
    from django.conf.urls import include
    from APP_NAME import urls as APP_NAME_urls

    urlpatterns = [
        path('admin/', admin.site.urls),
        path("", include(APP_NAME_urls, namespace="APP_NAME"))
    ]

Set a template location for the "homepage.html" created in the view
in the project's template settings in PROJECT_NAME/settings.py:

    PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ...
    'DIRS': [os.path.join(PROJECT_DIR, 'APP_NAME/templates')]

Add a homepage.html file to APP_NAME/templates.

It is also possible to add the file to the PROJECT_NAME/templates/PROJECT_NAME.
In this case, the template_name property in the HomePage view should be set to:
    homepage_name =  "APP_NAME/homepage.html"

In this case, the APP_NAME is the namespace.
No changes need to be made to APP_NAME/settings.py.


The context_object_name indicated in the view can be used in the homepage.html to loop through the records.


### Add Authentication

    pipenv install django-allauth

In settings.py add to INSTALLED_APPS:
    'django.contrib.sites',
    'allauth', 
    'allauth.account',
    'allauth.socialaccount',

Add allauth settings to the bottom of the file:

    SITE_ID = 1
    LOGIN_URL = '/login'
    LOGIN_REDIRECT_URL = '/'
    ACCOUNT_AUTHENTICATION_REQUIRED = 'email'
    ACCOUNT_CONFIRM_EMAIL_ON_GET = True
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = "optional"
    ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
    ACCOUNT_LOGOUT_ON_GET = True
    ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
    ACCOUNT_LOGOUT_REDIRECT = '/'
    ACCOUNT_PRESERVE_USERNAME_CASING = False
    ACCOUNT_SESSION_REMEMBER = True
    ACCOUNT_SIGNUP_PASSWORD_TWICE = True
    ACCOUNT_USERNAME_MIN_LENGTH = 2
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend")

Include in PROJECT_NAME/urls.py:

    path('', include('allauth.urls')),

