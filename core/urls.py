from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # URL da Página Inicial (adicione uma view para ela se quiser)
    path('', views.home_view, name='home'),

    # URLs de Autenticação e CRUD de Usuário
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', views.SignUpView.as_view(), name='registro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('perfil/deletar/', views.deletar_conta_view, name='deletar_conta'),

    # URLs do CRUD de Endereços (Multi-Tabela)
    path('meus-enderecos/', views.gerenciar_enderecos, name='gerenciar_enderecos'),
    path('meus-enderecos/adicionar/', views.adicionar_endereco, name='adicionar_endereco'),
    path('meus-enderecos/editar/<int:endereco_id>/', views.editar_endereco, name='editar_endereco'),
    path('meus-enderecos/deletar/<int:endereco_id>/', views.deletar_endereco, name='deletar_endereco'),

    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/atualizar/', views.atualizar_carrinho, name='atualizar_carrinho'),

    # NOVA URL PARA O COMPRAR AGORA
   path('comprar-agora/<int:produto_id>/', views.comprar_agora, name='comprar_agora'),

    path('checkout/fechar-pedido/', views.fechar_pedido, name='fechar_pedido'),
    path('pedido/confirmado/<int:pedido_id>/', views.pedido_confirmado, name='pedido_confirmado'),
    path('meus-pedidos/', views.meus_pedidos, name='meus_pedidos'),
    path('produto/<int:produto_id>/', views.produto_detalhe, name='produto_detalhe'),

    path('busca/', views.busca, name='busca'),

    path('favoritos/', views.ver_favoritos, name='ver_favoritos'),
    path('favoritos/toggle/<int:produto_id>/', views.toggle_favorito, name='toggle_favorito'),

    # --- URLS DE RECUPERAÇÃO DE SENHA ---
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='core/registration/password_reset_form.html'), 
        name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='core/registration/password_reset_done.html'),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='core/registration/password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='core/registration/password_reset_complete.html'),
        name='password_reset_complete'),
    
     path('checkout/', views.checkout_page, name='checkout_page'),
]
