=====
Calc
=====

Calc is a simple Django app to calculate same expression.

Quick start
-----------

1. Add "calc" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'calc',
    )

2. Add values for email sending to your EMAIL_USE_TLS, EMAIL_HOST and
    EMAIL_PORT setting like this::

    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587


3. Include the calc URLconf in your project urls.py like this::

    url(r'^calc/', include('calc.urls')),

4. Run `python manage.py migrate` to create the calc models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a calc (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/calculator/ to participate in the calc.