# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""Specifies static assets (CSS, JS) required by the CATMAID front-end.

This module specifies all the static files that are required by the
CATMAID front-end. The configuration is separated in libraries and CATMAID's
own files:

Libraries: To add a new library, add a new entry into the libraries_js
dictionary and, if needed, add the libraries CSS files to sourcefiles
tuple of the 'library' entry in the ``STYLESHEETS`` dictionary.

CATMAID files: By default all CSS files in the ``static/css`` directory are
included as well as all JavaScript files in ``static/js`` and CATMAID's
subdirectories in it. However, if you want to add new files explicitly, add
CSS to the source_filenames tuple in the 'catmaid' entry of the ``STYLESHEETS``
dictionary. JavaScript files go into the 'catmaid' entry of the ``JAVASCRIPT``
dictonary at the end of this file.
"""

from collections import OrderedDict

STYLESHEETS = OrderedDict()

STYLESHEETS['{{ cookiecutter.app_name }}'] = {
    'source_filenames': (
        '{{ cookiecutter.app_name }}/css/*'
    ),
    'output_filename': 'css/{{ cookiecutter.app_name }}.css'
}

JAVASCRIPT = OrderedDict()

JAVASCRIPT['{{ cookiecutter.app_name }}'] = {
    'source_filenames': (
        '{{ cookiecutter.app_name }}/js/*',
    ),
    'output_filename': 'js/{{ cookiecutter.app_name }}.js'
}
