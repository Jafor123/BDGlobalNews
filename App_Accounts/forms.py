from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from App_Accounts.models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=11, required=False)

    class Meta:
        model = User
        fields = ('username','email', 'phone', 'password1', 'password2',)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileUpdateForm(forms.ModelForm):
    about = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 3,
        'cols': 40,
        'padding': '10px',
    }))

    class Meta:
        model = Profile
        fields = ('phone', 'country', 'city', 'address', 'about', 'fb_id', 'tw_id', 'instra_id', 'linkd_id', 'photo')
