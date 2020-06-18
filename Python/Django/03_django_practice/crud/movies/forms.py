from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label = '영화명',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-title form-control',
                'placeholder' : 'Enter the title',
            }
        )
    )
    title_en = forms.CharField(
        label = '영화명(영문)',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-title_en form-control',
                'placeholder' : 'Enter the title_en',
            }
        )
    )
    audience = forms.CharField(
        label = '누적 관객수',
        widget = forms.NumberInput(
            attrs = {
                'class' : 'my-audience form-control',
                'placeholder' : 'Enter the audience',
            }
        )
    )
    open_date = forms.CharField(
        label = '개봉일',
        widget = forms.DateInput(
            attrs = {
                'class' : 'my-open-date form-control',
                'placeholder' : 'Enter the open_date',
            }
        )
    )
    genre = forms.CharField(
        label = '장르',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-genre form-control',
                'placeholder' : 'Enter the genre',
            }
        )
    )
    watch_grade = forms.CharField(
        label = '장르',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-watch-grade form-control',
                'placeholder' : 'Enter the watch-grade',
            }
        )
    )
    description = forms.CharField(
        label = '세부내용',
        widget = forms.Textarea(
            attrs = {
                'class' : 'my-description form-control',
                'placeholder' : 'Enter the Description',
            }
        )
    )