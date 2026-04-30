# core/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Atividade

def home(request):
    """
    VIEW TRADICIONAL (Conecta com Front 1º Bim):
    Processa o formulário e renderiza o HTML completo.
    """
    if request.method == 'POST':
        # Segurança: O Django limpa esses dados contra SQL Injection automaticamente
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        Atividade.objects.create(titulo=titulo, descricao=descricao)
        return redirect('home')

    atividades = Atividade.objects.all().order_by('-criado_em')
    return render(request, 'home.html', {'atividades': atividades})

def api_atividades(request):
    """
    VIEW API (Conecta com Front 2º Bim):
    Entrega apenas DADOS brutos para Frameworks como React/Vue.
    """
    dados = list(Atividade.objects.values('id', 'titulo', 'descricao', 'criado_em'))
    # safe=False permite que enviemos uma lista (array) via JSON
    return JsonResponse(dados, safe=False)