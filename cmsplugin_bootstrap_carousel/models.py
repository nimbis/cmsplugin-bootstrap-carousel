# -*- coding: utf-8 -*-

from __future__ import absolute_import

from os.path import dirname

from django.conf import settings

if 'filer' in settings.INSTALLED_APPS:
    execfile(dirname(__file__)+"/models_filer.py")
else:
    execfile(dirname(__file__)+"/models_default.py")
