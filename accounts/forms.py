from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from accounts.models import UserProfile


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True,
                             label="",
                             widget=forms.TextInput(attrs={
                                 'class': 'mb-2',
                                 'placeholder': 'Email'
                             }))
    username = forms.CharField(required=True,
                               label="",
                               widget=forms.TextInput(attrs={
                                   'class': 'mb-2',
                                   'placeholder': 'Username'
                               }))
    password1 = forms.CharField(required=True,
                                label="",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'mb-2',
                                    'placeholder': 'Password'
                                }))
    password2 = forms.CharField(required=True,
                                label="",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'mb-2',
                                    'placeholder': 'Confirm Password'
                                }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = UserProfile
        exclude = ('user',)


class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]
