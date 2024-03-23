from django import forms

from apps.models import Contact
from captcha.fields import CaptchaField

class contactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()