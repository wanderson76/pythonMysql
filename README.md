# pythonMysql
Projeto Math-Backend: Portal de Atividades
Este é um projeto pedagógico que conecta os fundamentos de Back-End (Python/Django/MySQL) com as necessidades de um Front-End moderno.

Backlog do Projeto (Metodologia Ágil - Kanban)

Para desenvolver este sistema, seguimos estas etapas:

[x] Configuração de Infra: Setup do Codespace e ativação do serviço MySQL.

[x] Modelagem de Dados: Criação da tabela Atividade via Django ORM.

[x] Camada de Visão (MVT): Desenvolvimento da lógica de salvamento e listagem.

[ ] Entrega de Dados (API): Disponibilização de endpoint JSON para o Front-End (2º Bimestre).

[ ] Gestão de Qualidade: Refatoração de código e documentação.

Tecnologias Utilizadas

Linguagem: Python 3.12

Framework: Django 5.x

Banco de Dados: MySQL (SGBD Relacional)

Interface: Bootstrap 5 (CDN)

Como Replicar este Projeto (Guia do Aluno)

1. Preparação do Ambiente

Inicie o serviço do banco de dados e instale as dependências:

Bash
sudo service mysql start
pip install django mysqlclient

2. Configuração do MySQL
Crie o banco de dados e aplique as migrações do Django:

Bash
sudo mysql -u root -e "CREATE DATABASE IF NOT EXISTS math_db;"
python manage.py makemigrations
python manage.py migrate

3. Execução
Rode o servidor de desenvolvimento:

Bash
python manage.py runserver

Conectando com o Front-End (Pincelada 2º Bimestre)
O diferencial deste projeto é que ele não entrega apenas páginas HTML, mas também dados puros.

Endpoint de API
Acesse /api/ para ver os dados brutos vindos do MySQL. Este é o formato que frameworks como React e Vue.js utilizam para construir interfaces dinâmicas.

Exemplo de consumo via JavaScript:

JavaScript
// O Front-End pede os dados para o seu Back-End assim:
fetch('/api/')
    .then(res => res.json())
    .then(dados => console.log("Dados do MySQL:", dados));

Segurança e Boas Práticas
SQL Injection: Protegido via Django ORM.

CSRF Token: Proteção contra falsificação de requisições entre sites.

Versionamento: Uso de Git para rastreabilidade de alterações.

Atividades de Evolução
Branching: Crie uma nova branch para adicionar o campo dificuldade (Fácil, Média, Difícil) no Model.

Code Review: Analise o views.py de um colega e verifique a indentação.

Definition of Done: O projeto só é considerado pronto após o git push final.