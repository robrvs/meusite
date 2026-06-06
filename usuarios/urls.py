from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('home/', views.home, name='home'),
    path('lancar/', views.lancarNotas, name='lancar'),
    path('alterar/', views.alterar, name='alterar'),
    path('visualizar/', views.visualizar, name='visualizar'),
    path('logout/', views.logout_view, name='logout'),
    path('excluir_verificacao/<int:pk>/', views.excluir_verificacao, name='excluir_verificacao'),
   path('excluir/<int:pk>/', views.excluir, name='excluir'),
   path('editar_verificacao/<int:pk>/', views.editar_verificacao, name='editar_verificacao'),
   path('editar/<int:pk>/', views.editar, name='editar'),
]   
