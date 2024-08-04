from typing import Any
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from . forms import TodoForm
from . models import Todo
from django.views.generic import DeleteView,UpdateView,CreateView,ListView,DetailView

class index(ListView):
    model = Todo
    template_name = 'app_todo/index.html'
    context_object_name = "todos"

class add_todo(CreateView):
    model = Todo
    template_name = 'app_todo/add_todo.html'
    form_class = TodoForm
    success_url = '/'
    context_object_name = "form"


class complete_todo(UpdateView):
    def get(self,request,todo_id):
        todo = Todo.objects.get(id=todo_id)
        todo.completed = True
        todo.save()
        return redirect('index')

class delete_todo(DeleteView):
    def get(self,request,todo_id):
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('index')