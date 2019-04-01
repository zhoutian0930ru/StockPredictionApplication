
"""
WSGI config for stockprediction project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stockprediction.settings")

application = get_wsgi_application()
"""

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
import django

# assuming your django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/prateek/C++/StockPredictionApplication/stockprediction/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'stockprediction.settings'

# serve django via WSGI
from django.core.wsgi import get_wsgi_application
django.setup()
application = get_wsgi_application()
