# ==============================================================================
# IMPORTAÇÕES DE MÓDULOS E BIBLIOTECAS
# ==============================================================================
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# ==============================================================================
# DEFINIÇÃO DOS MODELOS
# ==============================================================================

class Produto(models.Model):
    """
    Representa um produto (esmalte, acessório, etc.) a ser vendido no e-commerce.
    """
    # --- Campos do Produto ---
    nome = models.CharField(max_length=100, help_text="Nome do produto.")
    descricao = models.TextField(help_text="Descrição detalhada do produto.")
    preco = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço de venda do produto.")
    marca = models.CharField(max_length=50, help_text="Marca do produto (ex: Risqué).")
    
    # ImageField requer a biblioteca 'Pillow' para funcionar.
    # 'upload_to' especifica o subdiretório dentro da pasta MEDIA onde as imagens serão salvas.
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, help_text="Imagem do produto.")

    def __str__(self):
        """
        Representação em string do objeto, usada principalmente no painel de administração.
        """
        return self.nome


class Usuario(AbstractUser):
    """
    Modelo de usuário customizado que herda do usuário padrão do Django (AbstractUser).
    Isso nos permite adicionar campos extras como CPF e telefone, mantendo todo o sistema de 
    autenticação, permissões e sessões do Django.
    """
    # --- Campos Adicionais do Usuário ---
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF', help_text="CPF do usuário, deve ser único.")
    telefone = models.CharField(max_length=15, blank=True, null=True, help_text="Telefone de contato do usuário.")
    
    # Campo de email, tornado obrigatório e único para ser usado no login.
    email = models.EmailField(unique=True)
    
    # Relacionamento Muitos-para-Muitos: um usuário pode favoritar vários produtos,
    # e um produto pode ser favoritado por vários usuários.
    # 'blank=True' permite que um usuário não tenha nenhum favorito.
    favoritos = models.ManyToManyField(Produto, related_name='favoritado_por', blank=True)
    
    # --- Configurações do Modelo de Usuário Customizado ---
    # Define que o campo 'email' será usado para o login, em vez do 'username'.
    USERNAME_FIELD = 'email'
    
    # Campos exigidos ao criar um superusuário pelo comando 'createsuperuser'.
    # 'username' ainda é necessário por compatibilidade com partes do Django.
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return reverse('perfil') # Retorna a URL da página de perfil


class EnderecoUsuario(models.Model):
    """
    Armazena os endereços de entrega associados a um usuário.
    """
    # Relacionamento Um-para-Muitos: um usuário pode ter vários endereços.
    # on_delete=models.CASCADE: Se o usuário for deletado, seus endereços também serão.
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='enderecos')
    
    # --- Campos do Endereço ---
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, help_text="Sigla do estado, ex: SP")
    cep = models.CharField(max_length=9, help_text="Formato 00000-000")

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}"


class Pedido(models.Model):
    """
    Representa um pedido finalizado pelo usuário, contendo o resumo da compra.
    """
    # Relacionamento com o usuário que fez o pedido.
    # on_delete=models.SET_NULL: Se o usuário for deletado, o pedido não será apagado,
    # mas o campo 'usuario' ficará nulo, preservando o histórico de vendas.
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Relacionamento com o endereço de entrega escolhido para este pedido.
    endereco_entrega = models.ForeignKey(EnderecoUsuario, on_delete=models.SET_NULL, null=True, blank=True)
    
    # --- Campos do Pedido ---
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    # auto_now_add=True: Preenche automaticamente com a data e hora no momento da criação.
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pendente', help_text="Status atual do pedido.")
    
    def __str__(self):
        # Exibe o nome do usuário se ele existir, senão exibe 'Convidado'.
        nome_usuario = self.usuario.first_name if self.usuario else 'Convidado'
        return f"Pedido {self.id} - {nome_usuario}"


class ItemPedido(models.Model):
    """
    Representa um item específico dentro de um Pedido.
    Funciona como a linha de uma nota fiscal.
    """
    # Relacionamento com o Pedido ao qual este item pertence.
    # related_name='itens': Permite acessar todos os itens a partir de um objeto Pedido (ex: meu_pedido.itens.all()).
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    
    # Relacionamento com o Produto que foi comprado.
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    
    # --- Campos do Item do Pedido ---
    quantidade = models.PositiveIntegerField(default=1)
    
    # Armazena o preço do produto NO MOMENTO DA COMPRA. Isso é crucial para que, 
    # mesmo se o preço do produto mudar no futuro, o histórico do pedido continue correto.
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} no Pedido {self.pedido.id}"
    

# core/models.py

class Cartao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cartoes')
    numero_cartao = models.CharField(max_length=19, help_text="Ex: 1234 5678 1234 5678")
    nome_titular = models.CharField(max_length=255)
    data_validade = models.CharField(max_length=5, help_text="MM/AA")
    # Por segurança, NUNCA armazenamos o CVV no banco de dados.
    # Este modelo é uma simplificação para fins de projeto.

    def __str__(self):
        # Mostra apenas os últimos 4 dígitos por segurança
        return f"Cartão final {self.numero_cartao[-4:]}"