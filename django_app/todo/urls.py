from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('delete/<todo_id>', views.delete, name='delete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
]
