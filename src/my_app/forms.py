from .models import Product, Review
from django.forms import ModelForm, TextInput, Textarea
from django import forms

class ReviewForm(forms.ModelForm):
    customer_name = forms.CharField(max_length=30, required=False)
    description = forms.CharField(max_length=30, required=False)

    class Meta:
        model = Review
        fields = ('customer_name', 'description')