from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Main Tance',
        'values': ['Some', 'Hello', '123']
    }
    return render(request, 'mainer/index.html', data)


def about(request):
    return render(request, 'mainer/about.html')
