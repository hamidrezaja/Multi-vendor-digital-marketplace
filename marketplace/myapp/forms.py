from django import forms
from .models import Product
from django.contrib.auth.models import User
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='رمز عبور',widget=forms.PasswordInput)
    password2=forms.CharField(label='تأیید رمز عبور',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','first_name']
    def check_password(self):
        if self.cleaned_data['password']!=self.cleaned_data['password2']:
           raise forms.ValidationError('فیلدهای رمز عبور مطابقت ندارند')
        return self.cleaned_data['password2']
    