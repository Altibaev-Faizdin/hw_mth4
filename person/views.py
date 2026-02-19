from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterResumeForm, LoginFormWithCaptcha
from django.utils.decorators import method_decorator
from django.views import generic
from django.urls import reverse, reverse_lazy




class RegisterView(generic.FormView):
    template_name = 'register.html'
    form_class = RegisterResumeForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = LoginFormWithCaptcha
    success_url = reverse_lazy('book_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProfileView(generic.TemplateView):
    template_name = 'profile.html'


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('login')



# def register_view(request):
#     if request.method == "POST":
#         form = RegisterResumeForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('profile')
#     else:
#         form = RegisterResumeForm()

#     return render(request, 'register.html', {'form': form})


# def login_view(request):
#     if request.method == "POST":
#         form = LoginFormWithCaptcha(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('book_list')
#     else:
#         form = LoginFormWithCaptcha()

#     return render(request, 'login.html', {'form': form})


# @login_required
# def profile_view(request):
#     return render(request, 'profile.html')


# def logout_view(request):
#     logout(request)
#     return redirect('login')
