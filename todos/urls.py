from django.urls import path, include
from . import views

urlpatterns = [
    # auth urls
    path('auth/',include('authenticate.urls')),
    path('', views.index, name="index"),
    path('view/<int:todo_id>', views.view, name="view"),
    path('delete/<int:todo_id>', views.delete, name="delete"),
    path('todo_completed/<int:todo_id>', views.todo_completed, name="todo_completed"),
    path('todo_pending/<int:todo_id>', views.todo_pending, name="todo_pending"),
    path('edit/<int:todo_id>', views.edit, name="edit"),
]