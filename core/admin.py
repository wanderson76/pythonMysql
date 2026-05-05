from django.contrib import admin
from .models import Atividade


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    # Isso faz aparecer colunas bonitas na listagem
    list_display = ("titulo", "criado_em")
    # Adiciona um campo de busca por título
    search_fields = ("titulo",)
