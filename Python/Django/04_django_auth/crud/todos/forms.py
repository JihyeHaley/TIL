from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    content = forms.CharField(
        widget = forms.TextInput(
            attrs = ({
                'class' : 'my-content form-control',
            })
        )
    )
    due_date = forms.CharField(
        widget = forms.TextInput(
            attrs = ({
                'class' : 'my-due_date form-control',
                'type' : 'date'
            })
        )
    )
    class Meta:
        model = Todo
        fields = ('content', 'due_date')
        # exclude = ('user',)