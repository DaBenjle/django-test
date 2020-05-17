from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList

def index(request, id):
    list = ToDoList.objects.get(id=id)
    return HttpResponse("Main View: " + list.__str__())
