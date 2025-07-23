from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import EnderecoUsuario
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'cpf', 'telefone')

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = EnderecoUsuario
        exclude = ('usuario',) # Exclui o campo de usuário do formulário

class CustomUserChangeForm(UserChangeForm):
    password = None # Remove o campo de senha da edição de perfil
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'telefone') # Campos que o usuário pode editar