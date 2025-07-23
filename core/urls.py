from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # URL da Página Inicial (adicione uma view para ela se quiser)
    # path('', views.index, name='index'), 

    # URLs de Autenticação e CRUD de Usuário
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', views.SignUpView.as_view(), name='registro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('perfil/deletar/', views.deletar_conta_view, name='deletar_conta'),

    # URLs do CRUD de Endereços (Multi-Tabela)
    path('meus-enderecos/', views.gerenciar_enderecos, name='gerenciar_enderecos'),
    path('enderecos/adicionar/', views.adicionar_endereco, name='adicionar_endereco'),
    # O '<int:pk>' captura o ID do endereço da URL
    path('enderecos/editar/<int:pk>/', views.editar_endereco, name='editar_endereco'),
    path('enderecos/deletar/<int:pk>/', views.deletar_endereco, name='deletar_endereco'),
]