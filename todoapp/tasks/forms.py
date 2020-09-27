from django import forms

from .models import ToDoItem


class AddTaskForm(forms.Form):
    description = forms.CharField(max_length=64, label='')


class ToDoItemFormModel(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ('description',)

