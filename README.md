Projeto DevOps - API de Gerenciamento de Tarefas
Este projeto demonstra um pipeline completo de CI/CD para uma aplicação Flask.

Funcionalidades
API REST para gerenciar tarefas
Containerização com Docker
Pipeline de CI/CD com GitHub Actions
Testes automatizados
Infraestrutura como Código
Como executar
Desenvolvimento local
# Clone o repositório
git clone <seu-repositorio>
cd meu-projeto-devops

# Configure ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt

# Execute a aplicação
python run.py


#1.testes no cmd power shell para criar uma tarefa:

$Body = @{titulo = 'Minha primeira tarefa'} | ConvertTo-Json
Invoke-RestMethod -Uri 'http://localhost:5000/tarefas' -Method Post -Body $Body -ContentType 'application/json'

#2. Listar todas as tarefas:

powershell
Invoke-RestMethod -Uri 'http://localhost:5000/tarefas' -Method Get

#3. Deletar a tarefa (substitua o ID se necessário):

powershell
Invoke-RestMethod -Uri 'http://localhost:5000/tarefas/1' -Method Delete

#4. Criar mais tarefas para testar:

powershell
$Body1 = @{titulo = 'Configurar GitHub Actions'} | ConvertTo-Json
Invoke-RestMethod -Uri 'http://localhost:5000/tarefas' -Method Post -Body $Body1 -ContentType 'application/json'

$Body2 = @{titulo = 'Testar Docker'} | ConvertTo-Json
Invoke-RestMethod -Uri 'http://localhost:5000/tarefas' -Method Post -Body $Body2 -ContentType 'application/json'
