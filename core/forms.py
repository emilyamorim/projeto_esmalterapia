from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Usuario, EnderecoUsuario, Cartao

class CustomUserCreationForm(UserCreationForm):
    # Definindo campos extras para ter mais controle
    first_name = forms.CharField(max_length=150, required=True, label='Nome')
    last_name = forms.CharField(max_length=150, required=True, label='Sobrenome')
    
    class Meta(UserCreationForm.Meta):
        model = Usuario
        # Define a ordem e quais campos aparecerão no formulário
        fields = ('first_name', 'last_name', 'email', 'cpf', 'telefone')
        
        # Define os rótulos (labels) em português para os campos do modelo
        labels = {
            'email': 'E-mail',
            'cpf': 'CPF',
            'telefone': 'Telefone (Opcional)',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # O campo username é obrigatório pelo Django, mas não o queremos na tela de cadastro.
        # Então, o escondemos e podemos preenchê-lo automaticamente.
        if 'username' in self.fields:
            self.fields['username'].widget = forms.HiddenInput()
            self.fields['username'].required = False

    def save(self, commit=True):
        user = super().save(commit=False)
        # Preenche o username com o email para garantir que seja único
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = EnderecoUsuario
        exclude = ('usuario',) # Exclui o campo de usuário do formulário

class CustomUserChangeForm(UserChangeForm):
    password = None  # Remove o campo de senha da edição de perfil

    class Meta:
        model = Usuario
        # 1. Adicionamos 'email' e 'cpf' para que apareçam no formulário
        fields = ('first_name', 'last_name', 'email', 'cpf', 'telefone')
        
        # 2. Traduzimos os rótulos para português
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'cpf': 'CPF',
            'telefone': 'Telefone',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 3. Tornamos os campos de email e cpf "read-only" (apenas leitura) por segurança
        # Isso faz com que eles apareçam preenchidos, mas desabilitados para edição.
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['cpf'].widget.attrs['readonly'] = True

class CartaoForm(forms.ModelForm):
    class Meta:
        model = Cartao
        exclude = ('usuario',)
        labels = {
            'numero_cartao': 'Número do Cartão',
            'nome_titular': 'Nome do Titular',
            'data_validade': 'Data de Validade (MM/AA)',
        }
