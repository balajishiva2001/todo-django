from django import forms
from . models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','description']
        widgets = {
            'title':forms.TextInput(attrs={"class":"form-control"}),
            'description':forms.Textarea(attrs={"class":"form-control"})
        }
        labels ={
            'title':'Enter your task title',
            'description':'Add your task description'
        }