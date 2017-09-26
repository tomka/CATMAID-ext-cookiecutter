# -*- coding: utf-8 -*-
"""Methods called by API endpoints"""
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def is_installed(request, project_id=None):
    """Check whether the extension {{ cookiecutter.project_name }} is installed."""
    return JsonResponse({'is_installed': True, 'msg': '{{ cookiecutter.project_name }} is installed'})
