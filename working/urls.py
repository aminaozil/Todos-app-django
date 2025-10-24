from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('todo/<int:pk>', views.todo_detail, name="todo_detail"),
    path("todo/new", views.todo_new, name="todo_new"),
    path('todo/<int:pk>/edit', views.todo_edit, name="todo_edit"),
    path('exercise/', views.exercise_list, name="exercise_list"),
    path('exercise/<int:pk>', views.exercise_detail, name="exercise_detail"),
    path('exercise/new', views.exercise_new, name='exercise_new'),
    path('exercise/<int:pk>/edit', views.exercise_edit, name='exercise_edit')
]
