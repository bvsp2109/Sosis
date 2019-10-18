from django import forms
from django.forms.utils import ValidationError
from .models import *

class FutureForm(forms.ModelForm):
    Name = forms.CharField(label='Full Name:', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    Aim = forms.CharField(label='Future Aim:', widget=forms.TextInput(attrs={'placeholder': 'Car, Bike, House'}))
    Email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email Id'}))
    Date = forms.DateField(label='Target Date:', widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))


    if not Email:
        raise ValidationError('Please enter Valid Email Address')
    if not Date:
        raise  ValidationError('Enter Valid Date')
    class Meta:
        model = Future
        fields = '__all__'
