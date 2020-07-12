from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    lat = forms.FloatField(
        widget = forms.HiddenInput()
    )

    lng = forms.FloatField(
        widget = forms.HiddenInput()
    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('lat', 'long',)
        # 이걸 해버리면... 아예 데이터를 받아올 수 없는거다.
