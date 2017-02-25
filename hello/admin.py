from django.conf import settings
from django.contrib import admin

from .models import Greetee, VisitorLog

admin.site.register(Greetee)
if getattr(settings, 'GREETER_LOG', False):
    admin.site.register(VisitorLog)
