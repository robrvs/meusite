import email

from django.shortcuts import render, redirect
from django.http.response import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout as logout_django

from usuarios.models import Nota
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    else:
        email = request.POST['email']
        senha = request.POST['senha']

        user = authenticate(request, username=email, password=senha)

        if user is not None:
            login_django(request, user)
            return render(request, 'usuarios/home.html')
        else:
            return HttpResponse('e-mail ou senha inválidos.')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')

    else:
        username = request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        first_name = request.POST.get('nome')

        user = User.objects.filter(username=email).first()

        if user:
            return HttpResponse('Usuário já existe!')

        else:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name
            )

            user.save()

            return HttpResponse('Usuário cadastrado com sucesso!')
        
def home(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/home.html')
    else:
        return HttpResponse('Faça o login para acessar!')

def lancarNotas(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'usuarios/lancarNotas.html')
        else:
            return HttpResponse('Faça o login para acessar!')
    else: # POST
        nota = Nota()
        nota.nome_aluno = request.user.first_name
        nota.disciplina = request.POST.get('disciplina')
        nota.nota_atividades = request.POST.get('nota_atividades')
        nota.nota_trabalho = request.POST.get('nota_trabalho')
        nota.nota_prova = request.POST.get('nota_prova')
        nota.media = int(nota.nota_atividades) + int(nota.nota_trabalho) + int(nota.nota_prova) // 3
        nota_verificada = Nota.objects.filter(disciplina=nota.disciplina).first()
        if nota_verificada:
            return HttpResponse('Disciplina já possui notas cadastradas!')
        else:
            nota.save()
            return render(request, 'usuarios/home.html')

def alterar(request):
    if request.user.is_authenticated:
        lista_notas = Nota.objects.all()
        dicionario_notas = {'lista_notas': lista_notas}
        return render(request, 'usuarios/alterarNotas.html', dicionario_notas)
    else:
        return HttpResponse('Faça o login para acessar!')

def visualizar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            lista_Notas = Nota.objects.all()
            dicionario_notas = {'lista_notas': lista_Notas}
            return render(request, 'usuarios/visualizarNotas.html', dicionario_notas)
        else:
            return HttpResponse('Faça o login para acessar!')
    else:
        disciplina = request.POST.get('disciplina')
        if disciplina == 'Todas as disciplinas':
            lista_Notas = Nota.objects.all()
        else:
            lista_Notas = Nota.objects.filter(disciplina=disciplina)
        dicionario_notas = {'lista_notas': lista_Notas}
        return render(request, 'usuarios/visualizarNotas.html', dicionario_notas)
    
def editar(request, pk):
        if request.method == "POST":
            if request.user.is_authenticated:
                nome_aluno = request.user.first_name
                disciplina = request.POST.get('disciplina')
                nota_atividades = request.POST.get('nota_atividades')
                nota_trabalho = request.POST.get('nota_trabalho')
                nota_prova = request.POST.get('nota_prova')
                media = int(nota_atividades) + int(nota_trabalho) + int(nota_prova)
                Nota.objects.filter(pk=pk).update(nome_aluno=nome_aluno, disciplina=disciplina, nota_atividades=nota_atividades,nota_trabalho=nota_trabalho, nota_prova=nota_prova, media=media)
                return HttpResponseRedirect(reverse('alterar'))
    
def editar_verificacao(request, pk):
        if request.method == "GET":
            if request.user.is_authenticated:
                lista_notas = Nota.objects.get(pk=pk)
                dicionario_notas = {'lista_notas': lista_notas}
                return render(request, 'usuarios/editar.html', dicionario_notas)
            else:
                return HttpResponse('Faça o login para acessar!')    
    
def excluir_verificacao(request, pk):
        if request.method == "GET":
            if request.user.is_authenticated:
                lista_notas = Nota.objects.get(pk=pk)
                dicionario_notas = {'lista_notas': lista_notas}
                return render(request, 'usuarios/excluir.html', dicionario_notas)
            else:
                return HttpResponse('Faça o login para acessar!')
            
def excluir(request, pk):
        if request.method == "GET":
            if request.user.is_authenticated:
                disciplina_selecionada = Nota.objects.get(pk=pk)
                disciplina_selecionada.delete()
                return HttpResponseRedirect(reverse('alterar'))
            else:
                return HttpResponse('Faça o login para acessar!')

def logout_view(request):
    if request.user.is_authenticated:
        logout_django(request)
        return render(request, 'usuarios/login.html')
    else:
        return HttpResponse('Você não acessou sua conta ainda!!')
    

