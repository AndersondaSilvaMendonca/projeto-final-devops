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

#### Clone o repositório
git clone < seu-repositorio >
<br/>
cd meu-projeto-devops

#### Configure ambiente virtual
python -m venv venv - no Windows powershell<br/>
python3 -m venv venv - no Linux <br/>
source venv/bin/activate  - no Linux/Mac <br/>
venv\Scripts\activate  - no Windows powershell

#### Instale dependências

pip install -r requirements.txt

#### Execute a aplicação
python run.py - no Windows powershell <br/>
python3 run.py - no Linux

Pode ser que precise instalar no ambiente linux debian/ubuntu/mint o python3-venv para funcionar o projeto no linux, a versão pode ser que peça a mais recente: 
apt install python3.10-venv 


#### 1. Testes no cmd power shell para criar uma tarefa:
No powershell <br/>
$Body = @{titulo = 'Minha primeira tarefa'} | ConvertTo-Json
Invoke-RestMethod -Uri 'http://localhost:5000/tarefas' -Method Post -Body $Body -ContentType 'application/json'

#### 2. Listar todas as tarefas:

No powershell <br/>
Invoke-RestMethod -Uri 'http://localhost:5000/tarefas' -Method Get

#### 3. Deletar a tarefa (substitua o ID se necessário):

No powershell <br/>
Invoke-RestMethod -Uri 'http://localhost:5000/tarefas/1' -Method Delete

#### 4. Criar mais tarefas para testar:

No powershell <br/>
$Body1 = @{titulo = 'Configurar GitHub Actions'} | ConvertTo-Json
Invoke-RestMethod -Uri 'http://localhost:5000/tarefas' -Method Post -Body $Body1 -ContentType 'application/json' <br/>
No powershell <br/>
$Body2 = @{titulo = 'Testar Docker'} | ConvertTo-Json
Invoke-RestMethod -Uri 'http://localhost:5000/tarefas' -Method Post -Body $Body2 -ContentType 'application/json'


#### 5. Colocar como concluida

No powershell <br/>
$BodyUpdate = @{concluida = $true} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:5000/tarefas/11" -Method Put -Body $BodyUpdate -ContentType 'application/json' -Headers @{'Accept' = 'application/json'}


### Containerize sua aplicação:
Tem que ter o docker instalado na maquina local <br/><br/>
Comandos usando powershell
#### Na pasta do seu projeto
docker build -t minha-api-tarefas .

#### Execute
docker run -p 5000:5000 minha-api-tarefas

Teste a API no container: <br/>
No powershell:<br/>
Invoke-RestMethod -Uri 'http://localhost:5000/health' -Method Get

Use os mesmos comandos que foram usados acima, antes de Containerizar.



