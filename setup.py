from setuptools import setup

setup(
    name='django_bootstrap_registration',
    version='0.1.1',
    author='Vijay Khemlani',
    author_email='vkhemlan@gmail.com',
    packages=[
        'bootstrap_registration',
        'bootstrap_registration.backends',
        'bootstrap_registration.forms',
    ],
    scripts=[],
    url='https://github.com/SoloTodo/django_bootstrap_registration',
    license='LICENSE.txt',
    description='Library that merges Django auth, registration and Bootstrap',
    long_description=open('README.rst').read(),
    install_requires=[
        'django-registration==0.8',
        ],
)
