from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    # 원래라면  forms.ModelForm
    # 내가 어떤 유저 모델을 가르키고 있는지를 알고 있어야 한다.
    # AUTH_USER_MODEL
    class Meta:
        model = get_user_model()
        fields = ('username', 'middlename',  'password1',  'password2', 'phone',)
