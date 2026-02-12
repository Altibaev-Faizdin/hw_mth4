from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField
from .models import Resume


class RegisterResumeForm(UserCreationForm):

    full_name = forms.CharField(label="ФИО")
    age = forms.IntegerField(label="Возраст")
    phone = forms.CharField(label="Телефон")
    email = forms.EmailField(label="Email")
    city = forms.CharField(label="Город")
    education = forms.CharField(label="Образование")
    experience = forms.CharField(widget=forms.Textarea, label="Опыт работы")
    skills = forms.CharField(widget=forms.Textarea, label="Навыки")
    about = forms.CharField(widget=forms.Textarea, label="О себе")
    desired_position = forms.CharField(label="Желаемая должность")
    github = forms.URLField(required=False, label="GitHub")

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'full_name',
            'age',
            'phone',
            'email',
            'city',
            'education',
            'experience',
            'skills',
            'about',
            'desired_position',
            'github',
        ]


class LoginFormWithCaptcha(AuthenticationForm):
    captcha = CaptchaField()