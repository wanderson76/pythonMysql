# core/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Atividade
import math

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

def resolver_quadratica(request):
    try:
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        c = float(request.GET.get('c', 0))

        if a == 0:
            return JsonResponse({'erro': 'O coeficiente "a" não pode ser zero em uma função quadrática.'}, status=400)

        delta = (b**2) - (4*a*c)
        raizes = []
        tipo_raiz = ""

        # Lógica de classificação das raízes (Delta)
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            raizes = [round(x1, 2), round(x2, 2)]
            tipo_raiz = "Duas raízes reais e distintas (A curva corta o eixo X em dois pontos)."
        elif delta == 0:
            x1 = -b / (2*a)
            raizes = [round(x1, 2)]
            tipo_raiz = "Uma única raíz real (A curva apenas encosta no eixo X)."
        else:
            raizes = []
            tipo_raiz = "Não existem raízes reais (A curva não toca o eixo X)."

        xv = -b / (2*a)
        yv = -delta / (4*a)

        return JsonResponse({
            'equacao': f'{a}x² + ({b})x + ({c}) = 0',
            'delta': delta,
            'tipo_raiz': tipo_raiz,
            'raizes': raizes,
            'vertice': {'xv': round(xv, 2), 'yv': round(yv, 2)},
            'concavidade': 'Para cima (Mínimo)' if a > 0 else 'Para baixo (Máximo)'
        })

    except (ValueError, TypeError):
        return JsonResponse({'erro': 'Parâmetros inválidos.'}, status=400)