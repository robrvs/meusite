from django.shortcuts import render
from django.http.response import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django  


def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    if request.method == 'POST':
        email = request.POST('email')
        senha = request.POST('senha')
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login_django(request, user)  
            return HttpResponse('Login autenticado com sucesso!')
        else:
            return HttpResponse('e-mail ou senha inválidos.')