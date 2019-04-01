import os
import requests
from io import StringIO
from django.utils.six.moves import range
from django.core.management.base import BaseCommand
from django.utils.encoding import force_text
from django.conf import settings
from django.core.files import File
from schema.models import Stocks
