from django import forms
from .models import FoodCategory, FoodChoice


class FoodCategoryForm(forms.ModelForm):
     class Meta:
         model = FoodCategory


class FoodChoiceForm(forms.ModelForm):
     class Meta:
         model = FoodChoice