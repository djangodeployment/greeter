from django.shortcuts import render


def home(request):
    context = {'greetee': 'world'}
    return render(request, 'hello/index.html', context)
