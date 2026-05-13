from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm

class LoginFormWithCaptcha(AuthenticationForm):
    captcha = CaptchaField()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'email', 'phone', 'birth_date', 'address', 'education', 
            'experience_years', 'desired_salary', 'skills', 'gender', 
            'resume_file', 'portfolio_image'
        )