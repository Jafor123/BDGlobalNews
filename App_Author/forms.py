from django import forms
from App_News.models import *


class CategoryApplyForm(forms.ModelForm):
    name = forms.CharField(label="Category Name")

    class Meta:
        model = Categoryapply
        fields = ['name']


class SubcategoryApplyForm(forms.ModelForm):
    name=forms.CharField(label="Sub Category Name")
    class Meta:
        model = Subcategoryapply
        fields = ['category', 'name',]


class NewsForm(forms.ModelForm):
    description = RichTextUploadingField()
    publish_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), initial=date.today)
    short_description = forms.CharField(label="Short Description", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'comm',
        'rows': 3,
        'cols': 40,
        'padding': '10px',
    }))

    class Meta:
        model = News
        fields = ('news_title', 'category', 'subcategory', 'description', 'short_description', 'thumbnail', 'draft',
                  'publish_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = Subcategory.objects.none()
        if 'category' in self.data:
            print(self.data.get('category'))
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by(
                    'name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.id:
            print("base id", self.instance.id)
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('name')
