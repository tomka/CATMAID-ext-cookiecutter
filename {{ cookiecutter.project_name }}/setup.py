#!/usr/bin/env python
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='{{ cookiecutter.project_name }}',
    version='0.0.1',
    packages=find_packages(exclude='travis'),
    include_package_data=True,
    license='{{ cookiecutter.license }}',
    description='A django app which acts as a drop-in extension for CATMAID.',
    long_description=README,
    url='https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        {% if cookiecutter.supports_py2 == 'y' -%}
        'Programming Language :: Python :: 2',
        {%- endif %}
        {% if cookiecutter.supports_py3 == 'y' -%}
        'Programming Language :: Python :: 3',
        {%- endif %}
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
