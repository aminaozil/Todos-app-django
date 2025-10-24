from django.shortcuts import render, get_object_or_404, redirect
from .models import Todos, Exercise
from .forms import TodoForm, ExerciseForm


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

def exercise_detail(request, pk):
    exos = get_object_or_404(Exercise, pk=pk)
    return render(request, 'exercise/exercise_detail.html', {'exos':exos})

def exercise_new(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exo = form.save(commit=False)
            exo.save()
            return redirect('exercise_detail', pk = exo.pk)
    else:
        form = ExerciseForm()

    return render(request, 'exercise/exercise_new.html', {'form':form})

def exercise_edit(request, pk):
    exo = get_object_or_404(Exercise, pk = pk)
    if request.method == "POST":
        form = ExerciseForm(request.POST, instance=exo)
        if form.is_valid():
            exo = form.save(commit=False)
            exo.save()
            return redirect('exercise_detail', pk = exo.pk)
    else:
        form = ExerciseForm(instance=exo)
        return render(request, 'exercise/exercise_new.html', {'form':form})  


        

