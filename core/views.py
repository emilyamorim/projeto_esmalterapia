from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import EnderecoUsuario, Usuario
from .forms import CustomUserCreationForm, CustomUserChangeForm, EnderecoForm
from .models import Produto

def home_view(request):
    produtos = Produto.objects.all()[:9] # Pega os 9 primeiros produtos
    context = {'produtos': produtos}
    return render(request, 'core/home.html', context)


# def home_view(request):
#     # Busca, por exemplo, os 9 primeiros produtos
#     produtos_destaque = Produto.objects.all()[:9] 
#     context = {
#         'produtos': produtos_destaque
#     }
#     return render(request, 'core/home.html', context)

# A view de registro (Class-Based View)
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'core/registro.html'

# View para gerenciar (listar) os endereços
@login_required
def gerenciar_enderecos(request):
    enderecos = EnderecoUsuario.objects.filter(usuario=request.user)
    return render(request, 'core/gerenciar_enderecos.html', {'enderecos': enderecos})

# View para adicionar um novo endereço
@login_required
def adicionar_endereco(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            endereco = form.save(commit=False)
            endereco.usuario = request.user
            endereco.save()
            return redirect('gerenciar_enderecos')
    else:
        form = EnderecoForm()
    # Adicionei a variável 'titulo' aqui também para consistência
    return render(request, 'core/form_endereco.html', {'form': form, 'titulo': 'Adicionar Novo Endereço'})

# View de Perfil (Read) e Edição (Update)
@login_required
def perfil_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect('perfil')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'core/perfil.html', {'form': form})

# View para Deletar Conta (Delete)
@login_required
def deletar_conta_view(request):
    if request.method == 'POST':
        usuario = request.user
        logout(request)
        usuario.delete()
        messages.success(request, 'Sua conta foi excluída com sucesso.')
        # É uma boa prática ter uma página inicial para redirecionar
        return redirect('login') # Redirecionando para login, pois 'index' não foi definida

    return render(request, 'core/deletar_conta_confirm.html')

# View de Editar Endereço (Update)
@login_required
def editar_endereco(request, pk):
    endereco = get_object_or_404(EnderecoUsuario, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = EnderecoForm(request.POST, instance=endereco)
        if form.is_valid():
            form.save()
            return redirect('gerenciar_enderecos')
    else:
        form = EnderecoForm(instance=endereco)
    return render(request, 'core/form_endereco.html', {'form': form, 'titulo': 'Editar Endereço'})

# View de Deletar Endereço (Delete)
@login_required
def deletar_endereco(request, pk):
    endereco = get_object_or_404(EnderecoUsuario, pk=pk, usuario=request.user)
    if request.method == 'POST':
        endereco.delete()
        return redirect('gerenciar_enderecos')
    return render(request, 'core/deletar_endereco_confirm.html', {'endereco': endereco})