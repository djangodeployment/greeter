import random

from django.shortcuts import render

from .models import Greetee


def home(request):
    try:
        greetee = random.choice(Greetee.objects.all()[:])
    except IndexError:
        greetee = 'world'
    context = {'greetee': greetee}
    return render(request, 'hello/index.html', context)
