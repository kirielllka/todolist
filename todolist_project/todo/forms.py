from django.forms import ModelForm

from todo.models import TodoModel


class TodoForm(ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'memo', 'important']


