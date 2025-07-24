# ==============================================================================
# IMPORTAÇÕES DE MÓDULOS E BIBLIOTECAS
# ==============================================================================

# Funções essenciais do Django para renderizar páginas, redirecionar e lidar com erros
from django.shortcuts import render, redirect, get_object_or_404

# Ferramentas para o sistema de autenticação e mensagens de feedback
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

# Ferramentas para Class-Based Views (CBV) e URLs
from django.views import generic
from django.urls import reverse_lazy

# Ferramenta para criar consultas complexas ao banco de dados (ex: OU lógico)
from django.db.models import Q

# Importação dos modelos e formulários da nossa aplicação 'core'
from .models import Produto, Usuario, EnderecoUsuario, Pedido, ItemPedido
from .forms import CustomUserCreationForm, CustomUserChangeForm, EnderecoForm


# ==============================================================================
# VIEWS DE PÁGINAS GERAIS E CATÁLOGO DE PRODUTOS
# ==============================================================================

def home_view(request):
    """
    Exibe a página principal (home) do site.
    Busca os 9 primeiros produtos cadastrados para exibi-los como destaque.
    """
    produtos = Produto.objects.all()[:9]
    context = {'produtos': produtos}
    return render(request, 'core/home.html', context)


def produto_detalhe(request, produto_id):
    """
    Exibe a página de detalhes de um produto específico.
    Busca o produto pelo seu ID; se não encontrar, retorna um erro 404.
    """
    produto = get_object_or_404(Produto, id=produto_id)
    context = {'produto': produto}
    return render(request, 'core/produto_detalhe.html', context)


def busca(request):
    """
    Processa a busca feita pelo usuário no cabeçalho.
    Filtra produtos cujo nome OU descrição contenham o termo pesquisado.
    """
    query = request.GET.get('q', '')  # Pega o termo de busca da URL (?q=...)
    
    if query:
        # Usa Q objects para criar uma consulta com 'OU' (OR)
        # '__icontains' faz a busca ser case-insensitive (ignora maiúsculas/minúsculas)
        resultados = Produto.objects.filter(
            Q(nome__icontains=query) | Q(descricao__icontains=query)
        )
    else:
        resultados = []  # Se a busca for vazia, retorna uma lista vazia

    context = {
        'query': query,
        'resultados': resultados
    }
    return render(request, 'core/resultados_busca.html', context)


# ==============================================================================
# VIEWS DE AUTENTICAÇÃO E CADASTRO DE USUÁRIO
# ==============================================================================

class SignUpView(generic.CreateView):
    """
    Página de cadastro de um novo usuário.
    Usa uma Class-Based View para simplificar a criação de um objeto.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redireciona para a página de login após o sucesso
    template_name = 'core/registro.html'


# ==============================================================================
# VIEWS DO PERFIL E GESTÃO DA CONTA DO USUÁRIO
# ==============================================================================

@login_required
def perfil_view(request):
    """
    Exibe e processa o formulário de edição dos dados pessoais do usuário.
    """
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect('perfil')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'core/perfil.html', {'form': form})


@login_required
def deletar_conta_view(request):
    """
    Processa a exclusão da conta do usuário logado.
    """
    if request.method == 'POST':
        usuario = request.user
        logout(request)  # Faz o logout antes de deletar para invalidar a sessão
        usuario.delete()
        messages.success(request, 'Sua conta foi excluída com sucesso.')
        return redirect('home')  # Redireciona para a página principal

    return render(request, 'core/deletar_conta_confirm.html')


# --- CRUD de Endereços do Usuário ---

@login_required
def gerenciar_enderecos(request):
    """ Exibe a lista de endereços do usuário logado. """
    enderecos = EnderecoUsuario.objects.filter(usuario=request.user)
    return render(request, 'core/gerenciar_enderecos.html', {'enderecos': enderecos})


@login_required
def adicionar_endereco(request):
    """ Processa a adição de um novo endereço. """
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            endereco = form.save(commit=False)
            endereco.usuario = request.user  # Associa o endereço ao usuário logado
            endereco.save()
            messages.success(request, 'Endereço adicionado com sucesso!')
            return redirect('gerenciar_enderecos')
    else:
        form = EnderecoForm()
    return render(request, 'core/form_endereco.html', {'form': form, 'titulo': 'Adicionar Novo Endereço'})


@login_required
def editar_endereco(request, endereco_id):
    """ Processa a edição de um endereço existente. """
    endereco = get_object_or_404(EnderecoUsuario, id=endereco_id, usuario=request.user)
    if request.method == 'POST':
        form = EnderecoForm(request.POST, instance=endereco)
        if form.is_valid():
            form.save()
            messages.success(request, 'Endereço atualizado com sucesso!')
            return redirect('gerenciar_enderecos')
    else:
        form = EnderecoForm(instance=endereco)
    return render(request, 'core/form_endereco.html', {'form': form, 'titulo': 'Editar Endereço'})


@login_required
def deletar_endereco(request, endereco_id):
    """ Processa a exclusão de um endereço. """
    endereco = get_object_or_404(EnderecoUsuario, id=endereco_id, usuario=request.user)
    if request.method == 'POST':
        endereco.delete()
        messages.success(request, 'Endereço excluído com sucesso!')
        return redirect('gerenciar_enderecos')
    return render(request, 'core/deletar_endereco_confirm.html', {'endereco': endereco})


# --- Lista de Favoritos do Usuário ---

@login_required
def toggle_favorito(request, produto_id):
    """
    Adiciona ou remove um produto da lista de favoritos do usuário.
    """
    produto = get_object_or_404(Produto, id=produto_id)
    if produto in request.user.favoritos.all():
        request.user.favoritos.remove(produto)
        messages.success(request, f'"{produto.nome}" foi removido dos seus favoritos.')
    else:
        request.user.favoritos.add(produto)
        messages.success(request, f'"{produto.nome}" foi adicionado aos seus favoritos.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))  # Redireciona para a página anterior


@login_required
def ver_favoritos(request):
    """ Exibe a página com a lista de produtos favoritados pelo usuário. """
    produtos_favoritos = request.user.favoritos.all()
    context = {'favoritos': produtos_favoritos}
    return render(request, 'core/favoritos.html', context)


# ==============================================================================
# VIEWS DO CARRINHO DE COMPRAS (Usa a Sessão do Django)
# ==============================================================================

@login_required
def adicionar_ao_carrinho(request, produto_id):
    """
    Adiciona uma unidade de um produto ao carrinho na sessão.
    Se o produto já existir, incrementa a quantidade.
    """
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho = request.session.get('carrinho', {})
    quantidade = carrinho.get(str(produto_id), 0)
    carrinho[str(produto_id)] = quantidade + 1
    request.session['carrinho'] = carrinho
    messages.success(request, f'"{produto.nome}" foi adicionado ao seu carrinho!')
    return redirect(request.META.get('HTTP_REFERER', 'home')) # Redireciona para a página anterior


@login_required
def ver_carrinho(request):
    """
    Exibe a página do carrinho de compras com todos os itens,
    quantidades e o subtotal.
    """
    carrinho_session = request.session.get('carrinho', {})
    carrinho_items = []
    subtotal = 0
    
    produto_ids = carrinho_session.keys()
    produtos = Produto.objects.filter(id__in=produto_ids)
    
    for produto in produtos:
        quantidade = carrinho_session[str(produto.id)]
        total_item = produto.preco * quantidade
        subtotal += total_item
        carrinho_items.append({
            'produto': produto,
            'quantidade': quantidade,
            'total_item': total_item,
        })
        
    context = {
        'carrinho_items': carrinho_items,
        'subtotal': subtotal
    }
    return render(request, 'core/carrinho.html', context)


@login_required
def remover_do_carrinho(request, produto_id):
    """ Remove completamente um item do carrinho. """
    carrinho = request.session.get('carrinho', {})
    produto_id_str = str(produto_id)
    if produto_id_str in carrinho:
        del carrinho[produto_id_str]
        messages.success(request, "Item removido do carrinho.")
    request.session['carrinho'] = carrinho
    return redirect('ver_carrinho')


@login_required
def atualizar_carrinho(request):
    """
    Aumenta ou diminui a quantidade de um item no carrinho.
    Se a quantidade chegar a zero, o item é removido.
    """
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        action = request.POST.get('action')  # 'increase' ou 'decrease'
        carrinho = request.session.get('carrinho', {})
        produto_id_str = str(produto_id)
        if produto_id_str in carrinho:
            if action == 'increase':
                carrinho[produto_id_str] += 1
            elif action == 'decrease':
                carrinho[produto_id_str] -= 1
                if carrinho[produto_id_str] <= 0:
                    del carrinho[produto_id_str]
        request.session['carrinho'] = carrinho
    return redirect('ver_carrinho')


# ==============================================================================
# VIEWS DO PROCESSO DE CHECKOUT E PEDIDOS
# ==============================================================================

@login_required
def comprar_agora(request, produto_id):
    """
    Limpa o carrinho, adiciona um único item e redireciona
    diretamente para a página de checkout.
    """
    produto = get_object_or_404(Produto, id=produto_id)
    request.session['carrinho'] = {} # Limpa o carrinho
    carrinho = request.session.get('carrinho', {})
    carrinho[str(produto.id)] = 1 # Adiciona 1 unidade do produto
    request.session['carrinho'] = carrinho
    return redirect('checkout_page')


@login_required
def checkout_page(request):
    """
    Exibe a página de checkout, mostrando o resumo do pedido e as opções
    de endereço de entrega.
    """
    carrinho_session = request.session.get('carrinho', {})
    if not carrinho_session:
        messages.info(request, "Seu carrinho está vazio.")
        return redirect('home')

    produto_ids = carrinho_session.keys()
    produtos = Produto.objects.filter(id__in=produto_ids)
    carrinho_items = []
    subtotal = 0
    for produto in produtos:
        quantidade = carrinho_session[str(produto.id)]
        total_item = produto.preco * quantidade
        subtotal += total_item
        carrinho_items.append({
            'produto': produto, 'quantidade': quantidade, 'total_item': total_item,
        })
    
    enderecos = EnderecoUsuario.objects.filter(usuario=request.user)
    
    context = {
        'carrinho_items': carrinho_items,
        'subtotal': subtotal,
        'enderecos': enderecos
    }
    return render(request, 'core/checkout.html', context)


@login_required
def fechar_pedido(request):
    """
    Processa o formulário da página de checkout.
    Cria um objeto 'Pedido' e 'ItemPedido' para cada item no carrinho,
    limpa o carrinho e redireciona para a confirmação.
    """
    if request.method == 'POST':
        carrinho_session = request.session.get('carrinho', {})
        if not carrinho_session:
            messages.error(request, "Seu carrinho está vazio.")
            return redirect('ver_carrinho')

        produto_ids = carrinho_session.keys()
        produtos_no_carrinho = Produto.objects.filter(id__in=produto_ids)
        valor_total = 0
        for produto in produtos_no_carrinho:
            quantidade = carrinho_session[str(produto.id)]
            valor_total += produto.preco * quantidade

        endereco_id = request.POST.get('endereco_id')
        if not endereco_id:
            messages.error(request, "Por favor, selecione um endereço de entrega.")
            return redirect('checkout_page')
        
        endereco_selecionado = get_object_or_404(EnderecoUsuario, id=endereco_id, usuario=request.user)

        novo_pedido = Pedido.objects.create(
            usuario=request.user,
            endereco_entrega=endereco_selecionado,
            valor_total=valor_total,
            status='Aguardando Pagamento'
        )

        for produto in produtos_no_carrinho:
            quantidade = carrinho_session[str(produto.id)]
            ItemPedido.objects.create(
                pedido=novo_pedido,
                produto=produto,
                quantidade=quantidade,
                preco_unitario=produto.preco
            )
            
        del request.session['carrinho']
        
        messages.success(request, 'Sua compra foi realizada com sucesso! Obrigado por comprar conosco.')
        
        return redirect('pedido_confirmado', pedido_id=novo_pedido.id)
    
    return redirect('home')


def pedido_confirmado(request, pedido_id):
    """ Exibe a página de "Obrigado" após uma compra bem-sucedida. """
    pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
    context = {'pedido': pedido}
    return render(request, 'core/pedido_confirmado.html', context)


@login_required
def meus_pedidos(request):
    """ Exibe o histórico de pedidos do usuário logado. """
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-data_pedido')
    context = {'pedidos': pedidos}
    return render(request, 'core/meus_pedidos.html', context)