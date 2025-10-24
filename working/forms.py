from django import forms
from .models import Todos, Exercise

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todos
        fields = ("name",)

class ExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        fields = ("name", "description",)
