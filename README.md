# Projeto DevOps - API de Gerenciamento de Tarefas

Este projeto demonstra um pipeline completo de CI/CD para uma aplicação Flask.

## Funcionalidades
- API REST para gerenciar tarefas
- Containerização com Docker
- Pipeline de CI/CD com GitHub Actions
- Testes automatizados
- Infraestrutura como Código

## Como executar

### Desenvolvimento local
```bash
# Clone o repositório
git clone <seu-repositorio>
cd meu-projeto-devops

# Configure ambiente virtual
python -m venv venv
python3 -m venv venv # Linux
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt

# Execute a aplicação
python run.py # Windows
python3 run.py # Linux

# Pode ser que precise instalar no ambiente linux debian/ubuntu/mint o python3-venv para funcionar o projeto no linux, a versão pode ser que peça a mais recente: 
apt install python3.10-venv 


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


#5. colocar como concluida
$BodyUpdate = @{concluida = $true} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:5000/tarefas/11" -Method Put -Body $BodyUpdate -ContentType 'application/json' -Headers @{'Accept' = 'application/json'}


Containerize sua aplicação:
Tem que ter o docker instalado na maquina local
powershell
# Na pasta do seu projeto
docker build -t minha-api-tarefas .

# Execute
docker run -p 5000:5000 minha-api-tarefas

1. Teste a API no container:
powershell
Invoke-RestMethod -Uri 'http://localhost:5000/health' -Method Get

#Só um teste no windows

