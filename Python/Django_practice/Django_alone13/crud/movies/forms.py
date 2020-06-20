from django import forms

from .models import Movies

class MoviesForm(forms.ModelForm):
    title = forms.CharField(
        label = 'Title: ',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-title form-control',
                'placeholder' : 'Enter the Title ',
            }
        )
    )
  
    class Meta:
        model = Movies
        fields = '__all__'
