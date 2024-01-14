
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput,TextInput


# Create a user/register

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['first_name','last_name','username', 'email','password1','password2']
    
# Authenticate the user
        
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    















