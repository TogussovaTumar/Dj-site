from django import forms
from rest_framework.exceptions import ValidationError

from .models import*

class AddTourForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Category is not selected"

    class Meta:
        model = Tour
        fields = ['name','slug', 'content', 'price', 'photo', 'is_published','country', 'cat']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'price': forms.TextInput(attrs={'cols': 60, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title)>200:
            raise ValidationError('Length out of the range')

        return title














    # name = forms.CharField(max_length=255, label="Header",widget=forms.TextInput(attrs={'class':'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL" )
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Content")
    # price = forms.CharField(max_length=255,label="Price")
    # is_published = forms.BooleanField(label="Publication", required=False)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Category", empty_label="Not Selected yet")



