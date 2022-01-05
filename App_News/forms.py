from django import forms
from App_News.models import *
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'comm',
        'rows': 3,
        'cols': 40,
        'padding': '10px',
        'placeholder': "Enter  your Text here",
    }))

    class Meta:
        model = Comment
        fields = ['content']


class UnauthCommentForm(forms.ModelForm):
    content = forms.CharField(label="Comment", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'comm',
        'rows': 3,
        'cols': 40,
        'padding': '10px',
        'placeholder': "Enter  your Text here",
    }))

    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
