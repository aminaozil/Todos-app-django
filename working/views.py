from django.shortcuts import render, get_object_or_404
from .models import Todos, Exercise

def todo_list(request):
    todos = Todos.objects.all()
    return render(request, 'todo/todo_list.html', {'todos':todos})

def todo_detail(request, pk):
    todos = get_object_or_404(Todos, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todos':todos})

def exercise_list(request):
    exos = Exercise.objects.all()
    return render(request, 'exercise/exercise_list.html',{'exos':exos})