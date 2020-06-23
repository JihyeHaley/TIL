# day10_authentic

## Authentication이란?

####  = 인증 로그인, 회원가입할 때 사용한다.



## 🔮 집고 넘어갈 점

##### - Login 은 Model이나 ModelForm를 만들 필요 없이 장고에서 불러와서 생성할 수 있다.

`UserCreationForm `<- 회원가입

`AuthenticationForm` <- 로그인

```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
```



##### -  Login, Logout

마찬가지로 함수로 로그인을 표현할 수가 있다.

```python
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
```





view함수에서 갖다주지 않아도 template에서 `{{ user }}`을 쓸 수 있다.

Actually they are conatined in the request





#### views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
```

##### signup

```python
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # model에 save가 맞다.
            return redirect('account:login')
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
```



##### login

```python
def login(request):
    if request.method == 'POST':
        # 구조가 UserCreationForm하고는 다르다.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # form.save()가 아니다. / login 함수를 갖다 쓰면된다.
            auth_login(request, form.get_user())
            # login 함수는 -> login(1번째이자-request, 2번째인자-user)
            return redirect('todos:index')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
```



##### logout

```python
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
```

