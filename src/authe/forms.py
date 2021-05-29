from .models import Author
from django import forms
# from django.forms import ModelForm, CharField, EmailField, forms

class AuthorForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False)
    password = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = Author
        fields = ('username', 'email', 'password' )

class LoginForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('username', 'password' )
