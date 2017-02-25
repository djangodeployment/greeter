from django.contrib import admin

from .models import Greetee, VisitorLog

admin.site.register(Greetee)
admin.site.register(VisitorLog)
