from django.shortcuts import render, get_object_or_404, redirect
from .models import Todos, Exercise
from .forms import TodoForm


def todo_list(request):
    todos = Todos.objects.all()
    return render(request, 'todo/todo_list.html', {'todos':todos})

def todo_detail(request, pk):
    todos = get_object_or_404(Todos, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todos':todos})

def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()

    return render(request, 'todo/todo_new.html', {'form':form})

def todo_edit(request, pk):
    todo = get_object_or_404(Todos, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_new.html', {'form': form})

def exercise_list(request):
    exos = Exercise.objects.all()
    return render(request, 'exercise/exercise_list.html',{'exos':exos})