=============================
django_bootstrap_registration
=============================

django_bootstrap_registration is a library that combines the 
features of the `default authentication application <https://docs.djangoproject.com/en/1.4/topics/auth/#module-django.contrib.auth>`_
of Django with the registration system of `django-registration <https://bitbucket.org/ubernostrum/django-registration/>`_,
overriding their default forms with ones that make use of the
`bootstrap application <https://github.com/earle/django-bootstrap>`_, which
makes them compatible with the `Bootstrap CSS Framework <http://twitter.github.com/bootstrap/>`_
.

Installation
============

The easiest way to install django_bootstrap_registration is using pip::

    pip install -e git+git://github.com/earle/django-bootstrap.git#egg=bootstrap

    pip install django_bootstrap_registration

Configuration
=============

Enable the admin, bootstrap, registration and bootstrap_registration apps in
your project settings. Make sure that your application appears before the rest::

    'YOUR_APPLICATION',
    'bootstrap',
    'registration',
    'bootstrap_registration',
    'django.contrib.admin',

In the URLs file of the project, append the following declaration::

    urlpatterns += patterns('',
        url(r'^accounts/',        
        include('bootstrap_registration.urls')),
    )

Demo
====

The source code includes a small Django project and client application that
makes use of the library, just download it and run the typical commands to run
a Django project::

    python manage.py syncdb
    python manage.py runserver

Its settings configuration show the installation and configuration steps
described above.