from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import ToDoList

def index(request):
    context = {}
    return render(request, 'main/base.html', context)

def special(request, num):
    context = {'num': num}
    return render(request, 'main/special.html', context)
