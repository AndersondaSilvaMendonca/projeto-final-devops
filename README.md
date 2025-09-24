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
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt

# Execute a aplicação
python app/__init__.py