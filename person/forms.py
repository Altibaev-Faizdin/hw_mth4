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

    def save(self, commit=True):
        user = super().save(commit=commit)

        Resume.objects.create(
            user=user,
            full_name=self.cleaned_data['full_name'],
            age=self.cleaned_data['age'],
            phone=self.cleaned_data['phone'],
            email=self.cleaned_data['email'],
            city=self.cleaned_data['city'],
            education=self.cleaned_data['education'],
            experience=self.cleaned_data['experience'],
            skills=self.cleaned_data['skills'],
            about=self.cleaned_data['about'],
            desired_position=self.cleaned_data['desired_position'],
            github=self.cleaned_data['github'],
        )

        return user


class LoginFormWithCaptcha(AuthenticationForm):
    captcha = CaptchaField()
