from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Produto, EnderecoUsuario, Pedido, ItemPedido

# --- Customização para o admin do seu Usuário ---
# Isso faz com que seus campos extras (cpf, telefone) apareçam no admin
class CustomUserAdmin(UserAdmin):
    # Campos a serem exibidos na lista de usuários
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')

    # Campos a serem exibidos ao editar um usuário
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Personalizados', {'fields': ('cpf', 'telefone')}),
    )

    # Campos a serem exibidos ao criar um novo usuário no admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Personalizados', {'fields': ('cpf', 'telefone')}),
    )

# --- Registrando os modelos ---
# Para cada modelo que você quer que apareça no admin,
# você precisa de uma linha admin.site.register()

admin.site.register(Usuario, CustomUserAdmin)
admin.site.register(Produto)
admin.site.register(EnderecoUsuario)
admin.site.register(Pedido)
admin.site.register(ItemPedido)