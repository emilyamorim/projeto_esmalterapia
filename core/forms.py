from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import EnderecoUsuario
from .models import Usuario

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
    password = None # Remove o campo de senha da edição de perfil
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'telefone') # Campos que o usuário pode editar