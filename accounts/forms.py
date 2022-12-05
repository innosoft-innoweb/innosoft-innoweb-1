from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

from participant.models import Participant

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Participant
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'photo']
   
