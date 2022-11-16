from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        model = Participant
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'photo']
    
    # def save(self, commit=True):
    #     user= super(RegisterForm, self).save(commit=False)
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']

    #     if commit:
    #         user.save()
    #     return user
