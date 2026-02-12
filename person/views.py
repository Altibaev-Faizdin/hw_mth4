from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterResumeForm, LoginFormWithCaptcha
from .models import Resume



def register_view(request):
    if request.method == "POST":
        form = RegisterResumeForm(request.POST)
        if form.is_valid():
            user = form.save()

            Resume.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                age=form.cleaned_data['age'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                city=form.cleaned_data['city'],
                education=form.cleaned_data['education'],
                experience=form.cleaned_data['experience'],
                skills=form.cleaned_data['skills'],
                about=form.cleaned_data['about'],
                desired_position=form.cleaned_data['desired_position'],
                github=form.cleaned_data['github'],
            )

            login(request, user)
            return redirect('profile')
    else:
        form = RegisterResumeForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginFormWithCaptcha(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = LoginFormWithCaptcha()

    return render(request, 'login.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'profile.html')


def logout_view(request):
    logout(request)
    return redirect('login')