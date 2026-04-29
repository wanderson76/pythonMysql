from django.shortcuts import render, redirect
from .models import Atividade

def home(request):
    if request.method == 'POST':
        # Pega os dados vindos do formulário
        titulo_form = request.POST.get('titulo')
        descricao_form = request.POST.get('descricao')
        
        # Salva no MySQL através do Django
        Atividade.objects.create(titulo=titulo_form, descricao=descricao_form)
        
        return redirect('home') # Recarrega a página para limpar o form

    atividades = Atividade.objects.all()
    return render(request, 'home.html', {'atividades': atividades})