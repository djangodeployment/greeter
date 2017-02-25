import random

from django.conf import settings
from django.shortcuts import render

from .models import Greetee, VisitorLog


def home(request):
    try:
        greetee = random.choice(Greetee.objects.all()[:])
    except IndexError:
        greetee = Greetee(name='world')
    if getattr(settings, 'GREETER_LOG', False):
        VisitorLog(greetee=greetee).save()
    context = {'greetee': greetee}
    return render(request, 'hello/index.html', context)
