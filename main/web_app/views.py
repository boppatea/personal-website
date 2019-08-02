from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'web_app/index.html')

def work(request):
    return render(request, 'web_app/work.html')
