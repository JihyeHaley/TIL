from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('user',)


class AnswerForm(forms.ModelForm):
    CHOICES = [
        ('a','RED'),
        ('b','BLUE'),
    ]
    choice = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Answer
        fields = ('choice',)