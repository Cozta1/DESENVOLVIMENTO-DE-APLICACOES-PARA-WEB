# Register your models here.
from django.contrib import admin

from .models import Cliente, Agencia, Conta, Transacao, Cartao, Endereco, Notificacao


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'cep', 'rua', 'bairro', 'cidade', 'estado', 'numero', 'complemento')
    search_fields = ('cliente', 'cep', 'rua', 'bairro', 'cidade')  # permite buscar pelos campos
    list_filter = ('cliente', 'estado', 'cidade')  # adiciona filtros na barra lateral
    
class EnderecoInline(admin.TabularInline):
    
    model = Endereco
    extra = 1  # Número de formulários em branco para adicionar novos endereços


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('CPF', 'first_name', 'last_name', 'email', 'telefone', 'listar_enderecos', 'foto')  
    search_fields = ('CPF', 'first_name', 'last_name', 'email', 'telefone')  # Campos pesquisáveis no admin
    ordering = ('CPF',)  # Ordenação padrão no admin
    list_filter = ('is_staff', 'is_active')  # Filtros adicionais
    readonly_fields = ('listar_enderecos',)  # Exibe os endereços, mas não permite edição direta
    inlines = [EnderecoInline]  # Permite gerenciar endereços diretamente no cliente
    fieldsets = (
        (None, {
            'fields': ('CPF', 'password')
        }),
        ('Informações pessoais', {
            'fields': ('first_name', 'last_name', 'email', 'telefone', 'foto')
        }),
        ('Permissões', {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

admin.site.register(Cliente, ClienteAdmin)
    

    
@admin.register(Agencia)
class AgenciaAdmin(admin.ModelAdmin):
    list_display = ('nomeagencia', 'numeroagencia', 'endereco')

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ('numeroConta', 'cliente', 'agencia', 'saldo', 'dataAbertura')
    
    def saldo(self, obj):
        return obj.saldo

    saldo.short_description = 'Saldo Atual'
    
@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('numeroTransacao', 'conta', 'tipoTransacao', 'valor', 'dataHora', 'status', 'contaDestino')
    list_filter = ('tipoTransacao', 'status')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('conta', 'contaDestino')  # Otimizar as consultas para evitar N+1

@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = ('numeroCartao', 'bandeira', 'cvv', 'dataExpiracao', 'conta')
    list_filter = ('bandeira', 'conta')


@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('conta', 'mensagem', 'dataHora')