from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # tuple로!
        fields = ('username', 'middlename','password1',  'password2', 'phone',)