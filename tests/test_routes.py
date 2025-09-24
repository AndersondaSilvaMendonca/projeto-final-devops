import pytest
import json
from app import create_app, db
from app.models import Tarefa

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_criar_tarefa(client):
    response = client.post('/tarefas', 
                         json={'titulo': 'Tarefa de teste'},
                         content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'id' in data
    assert data['titulo'] == 'Tarefa de teste'

def test_listar_tarefas(client):
    # Primeiro cria uma tarefa
    client.post('/tarefas', json={'titulo': 'Tarefa 1'})
    
    # Depois lista
    response = client.get('/tarefas')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['titulo'] == 'Tarefa 1'

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'