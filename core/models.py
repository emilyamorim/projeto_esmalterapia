from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

class EnderecoUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='enderecos')
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=45)
    complemento = models.CharField(max_length=200, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}"

# class Produto(models.Model):
#     idProduto = models.AutoField(primary_key=True)
#     nome = models.CharField(max_length=45)
#     descricao = models.CharField(max_length=200)
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     marca = models.CharField(max_length=45)
#     categoria = models.CharField(max_length=45)

#     def __str__(self):
#         return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    def __str__(self):
        return self.nome