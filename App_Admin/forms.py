from django import forms
from App_News.models import *
from App_Accounts.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','is_nav')


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ('category','name',)


class NewsAddForm(forms.ModelForm):
    description = RichTextUploadingField()
    publish_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}),initial=date.today)
    short_description = forms.CharField(label="Short Description", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
        'cols': 40,
        'padding': '10px',
    }))
    class Meta:
        model=News
        fields=['author','news_title','category','subcategory','description','short_description','thumbnail',
                'publish_date','publish','draft','spam','like',
                ]


class UserverifyListForm(forms.ModelForm):
    class Meta:
        model=UserVerify
        fields='__all__'


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'


class SubscriberForm(forms.ModelForm):
    class Meta:
        model=Subscriber
        fields='__all__'


class EditorForm(forms.ModelForm):
    class Meta:
        model=EditorList
        fields='__all__'


class ProfileForm(forms.ModelForm):
    about = forms.CharField(label="About", required=False,widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
        'cols': 40,
    }))
    fb_id=forms.URLField(label="Facebook Id",required=False)
    tw_id=forms.URLField(label="Twitter Id",required=False)
    linkd_id=forms.URLField(label="Linkedin Id",required=False)
    instra_id=forms.URLField(label="Instragam Id",required=False)
    class Meta:
        model=Profile
        fields='__all__'