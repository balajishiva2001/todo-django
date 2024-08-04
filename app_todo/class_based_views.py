from django.shortcuts import render,redirect
from . forms import TodoForm
from . models import Todo
from django.views import View


class index(View):
    template = 'app_todo/index.html'
    
    def get(self,request):
        todos = Todo.objects.all()
        return render(request,self.template,context={'todos':todos})
    

class add_todo(View):
    template = 'app_todo/add_todo.html'
    def get(self, request):
        form = TodoForm()
        return render(request,self.template,context={'form':form})
    
    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')

class complete_todo(View):

    def get(self,request,todo_id):
        todo = Todo.objects.get(id=todo_id)
        todo.completed = True
        todo.save()
        return redirect('index')

class delete_todo(View):
    def get(self,request,todo_id):
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('index')

