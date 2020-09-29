from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .forms import LoginForm


class LoginView(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])

            if user is None:
                return HttpResponse("Неправильный логин или пароль")

            login(request, user)
            return HttpResponse("Добро пожаловать, успешный вход")

        return render(request, 'accounts/login.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
