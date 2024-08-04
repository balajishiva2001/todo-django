
from django.contrib import admin
from django.urls import path
from . import views
from . import class_based_views
from . import generic_views

urlpatterns = [
    
    
    ####### These are the metjod based views ######## 
    path('', views.index,name='index'),
    path('add/', views.add_todo,name='add_todo'),
    path('complete/<int:todo_id>', views.complete_todo,name='complete_todo'),
    path('delete/<int:todo_id>', views.delete_todo,name='delete_todo'),
    

    ####### These are the class based views ######## 
    #path('', class_based_views.index.as_view(),name='index'),
    #path('add/', class_based_views.add_todo.as_view(),name='add_todo'),
    #path('complete/<int:todo_id>', class_based_views.complete_todo.as_view(),name='complete_todo'),
    #path('delete/<int:todo_id>',class_based_views.delete_todo.as_view(),name='delete_todo'),

    ####### These are the generic views ######## 
    #path('', generic_views.index.as_view(),name='index'),
    #path('add/', generic_views.add_todo.as_view(),name='add_todo'),
    #path('complete/<int:todo_id>', generic_views.complete_todo.as_view(),name='complete_todo'),
    #path('delete/<int:todo_id>',generic_views.delete_todo.as_view(),name='delete_todo'),
]
