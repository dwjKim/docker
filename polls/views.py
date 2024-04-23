from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

from .models import ToDoList


def index(request):
    todo_list = ToDoList.objects.all()
    template = loader.get_template('index.html')
    context = {
        'todo_list': todo_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, ToDoList_id):
    return HttpResponse("Your ToDoList is %s" % ToDoList_id)
