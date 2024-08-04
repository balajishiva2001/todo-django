from django.shortcuts import render,redirect
from . forms import TodoForm
from . models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request,'app_todo/index.html',{'todos':todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request,'app_todo/add_todo.html',{'form':form})

def complete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')

def delete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return redirect('index')