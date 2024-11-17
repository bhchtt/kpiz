from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'firstname', 'lastname', 'password1', 'password2']
