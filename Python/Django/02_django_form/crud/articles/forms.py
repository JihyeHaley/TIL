from django import forms
from .models import Article

#class ArticleForm (forms.Form):
#    title = forms.CharField(max_length=20)
#    # form 에는  TextField가 없다.
#    content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = "제목",
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-title form-control',
                'placeholder' : 'Enter the title.',
            }
        )
    )

    content = forms.CharField(
        label = "내용",
        widget = forms.Textarea(
            attrs = {
                'class' : 'my-content form-control',
                'placeholder' : 'Enter the content',
                'cols' : 40,
                'rows' : 10, 
            }
        )
    )

    # Meta : ArticleFomr에 대한 정보를 작성하는 곳 
    class Meta:
        model = Article
        #fields = ['title', 'content',]
        fields = '__all__'
