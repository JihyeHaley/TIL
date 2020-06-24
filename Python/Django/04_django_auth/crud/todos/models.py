from django.db import models
from django.conf import settings
# Create your models here.

class Todo(models.Model):
    content = models.CharField(max_length=100)
    due_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user 에는 number
    # User을 만들지 않았다. 그래서 어디선가 가져와야한다.
    # 뭐쓸지 말해주는 변수를 쓰면 나중에 뒤에 들어간느 이름이 바껴도 변수를 바꿀 필요가 없다.