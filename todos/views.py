from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        
        if form.is_valid():
            todo=form.save(commit=False)
            todo.created_by=request.user
            todo.save()
            todos = Todo.objects.filter(created_by=request.user)
            messages.success(request, ('Item has been added to the list.'))
            return render(request, 'todos/index.html', {'todos': todos})

    else:
        total_tasks=Todo.objects.filter(created_by=request.user).count()
        completed = Todo.objects.filter(created_by=request.user, completed=True).count()
        percent=completed/total_tasks*100
        todos = Todo.objects.filter(created_by=request.user)
        return render(request, 'todos/index.html', {'todos': todos, 'per':percent})

@login_required(login_url='login')
def view(request, todo_id):
    context = {
        'todo': Todo.objects.get(id=todo_id),
    }
    return render(request, 'todos/view.html', context)

@login_required(login_url='login')
def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, 'Item has been deleted.')
    return redirect('/')

@login_required(login_url='login')
def todo_pending(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('/')

@login_required(login_url='login')
def todo_completed(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('/')

@login_required(login_url='login')
def edit(request, todo_id):
    if request.method == 'POST':
        todos = Todo.objects.get(id=todo_id)

        form = TodoForm(request.POST or None, instance=todos)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited.'))
            return redirect('/')

    else:
        todos = Todo.objects.get(id=todo_id)
        return render(request, 'todos/edit.html', {'todos': todos})
