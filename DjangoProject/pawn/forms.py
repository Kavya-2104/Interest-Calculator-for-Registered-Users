from django import forms
from django.core.validators import validate_email

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {'first_name','last_name','amount','interest','month','phnno','email','collateral','address'}
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-group col-xs-4','type':'text' }),'last_name': forms.TextInput(attrs={
                'class': 'form-group col-xs-4' }),'email': forms.TextInput(attrs={
                'class': 'form-group col-xs-4' }),   'phnno': forms.TextInput(attrs={
                'class': 'form-group col-xs-4'  }), 'amount': forms.TextInput(attrs={
                'class': 'form-group col-xs-4' }), 'interest': forms.TextInput(attrs={
                'class': 'form-group col-xs-4'}),'month': forms.TextInput(attrs={
                'class': 'form-group col-xs-4' }),'collateral': forms.TextInput(attrs={
                'class': 'form-group col-xs-4' }),  'address': forms.TextInput(attrs={
                'class': 'form-group col-xs-5' }),
        }

        def __init__(self):
            self.cleaned_data = None

        def clean_email(self):
            email = self.cleaned_data.get("email")
            if not validate_email(email, verify=True):
                raise forms.ValidationError("Invalid email")
            return email

