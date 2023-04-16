from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from captcha.fields import CaptchaField

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

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1= forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2= forms.CharField(label='Confider  password',widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class ContactForm(forms.Form):
    name = forms.CharField(label='Name',max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows': 10}))
    captcha = CaptchaField()


    # name = forms.CharField(max_length=255, label="Header",widget=forms.TextInput(attrs={'class':'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL" )
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Content")
    # price = forms.CharField(max_length=255,label="Price")
    # is_published = forms.BooleanField(label="Publication", required=False)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Category", empty_label="Not Selected yet")



