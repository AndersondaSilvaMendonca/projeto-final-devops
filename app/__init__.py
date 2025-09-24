from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///todos.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    # Importar modelos DEPOIS de inicializar o db para evitar import circular
    from app.models import Tarefa
    
    # Rotas da API
    @app.route('/tarefas', methods=['GET'])
    def listar_tarefas():
        tarefas = Tarefa.query.all()
        return jsonify([tarefa.to_dict() for tarefa in tarefas])
    
    @app.route('/tarefas', methods=['POST'])
    def criar_tarefa():
        dados = request.get_json()
        nova_tarefa = Tarefa(titulo=dados['titulo'])
        db.session.add(nova_tarefa)
        db.session.commit()
        return jsonify(nova_tarefa.to_dict()), 201
    
    @app.route('/tarefas/<int:id>', methods=['DELETE'])
    def excluir_tarefa(id):
        tarefa = Tarefa.query.get_or_404(id)
        db.session.delete(tarefa)
        db.session.commit()
        return '', 204
    
    # Health check para monitoramento
    @app.route('/health')
    def health_check():
        return jsonify({'status': 'healthy'})
    
    @app.route('/')
    def index():
        return jsonify({'message': 'API de Tarefas funcionando!'})
    
    return app

# REMOVA esta parte do final do arquivo:
# if __name__ == '__main__':
#     app = create_app()
#     with app.app_context():
#         db.create_all()
#     app.run(host='0.0.0.0', port=5000, debug=False)