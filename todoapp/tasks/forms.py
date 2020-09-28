from django import forms
from .models import ToDoItem


class ToDoItemFormModel(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ('description',)
        labels = {'description': ''}


