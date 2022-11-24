from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.forms import TextInput, EmailField, CharField, PasswordInput

class LoginForm(AuthenticationForm):
    username = CharField(
        widget=TextInput(
            attrs={
                'type': 'text',
                'name': 'logname',
                'class':'form-style',
                'placeholder':'Ваш ник',
                'id':'logname',
                'autocomplete' : 'off'

            }
        )
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                'type':'password',
                'name':'logpass',
                'class': 'form-style',
                'placeholder':'Ваш пароль',
                'id':'logpass',
                'autocomplete':'off',
            }
        )
    )

class RegForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("username",)
        field_classes = {"username": UsernameField}

    username = CharField(
        widget=TextInput(
            attrs={
                'type': 'text',
                'name': 'logname',
                'class': 'form-style',
                'placeholder': 'Ваш ник',
                'id': 'logname',
                'autocomplete': 'off'

            }
        )
    )
    email = EmailField(
        widget=TextInput(
            attrs={
                'type': 'email',
                'name': 'logemail',
                'class': 'form-style',
                'placeholder': 'Ваша почта',
                'id': 'logemail',
                'autocomplete': 'off'

            }
        )
    )
    password1 = CharField(
        widget=PasswordInput(
            attrs={
                'type':'password',
                'name':'logpass',
                'class': 'form-style',
                'placeholder':'Ваш пароль',
                'id':'logpass',
                'autocomplete':'off',
            }
        )
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={
                'type':'password',
                'name':'logpass',
                'class': 'form-style',
                'placeholder':'Ваш пароль',
                'id':'logpass',
                'autocomplete':'off',
            }
        )
    )