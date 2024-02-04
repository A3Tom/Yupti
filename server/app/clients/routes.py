from flask import Blueprint, request, jsonify, make_response
from .models import Client
from .repository import ClientsRepository

client_repo = ClientsRepository()
clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/', methods=['POST'])
def create_client():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return make_response(jsonify({"error": "Name is required"}), 400)
    
    client = client_repo.create(Client(**data))
    return jsonify({'id': client.id, 'name': client.name}), 201

@clients_bp.route('/', methods=['GET'])
def get_clients():
    clients_list = client_repo.get_all()
    return jsonify([{'id': client.id, 'name': client.name} for client in clients_list]), 200

@clients_bp.route('/<int:id>', methods=['GET'])
def get_client(id):
    client = client_repo.get_by_id(id)
    if client is None:
        return jsonify({}), 204
    
    return jsonify({'id': client.id, 'name': client.name}), 200

@clients_bp.route('/<int:id>', methods=['PUT'])
def update_client(id):
    client = client_repo.update(id, request.get_json())    
    return jsonify({'id': client.id, 'name': client.name}), 200

@clients_bp.route('/<int:id>', methods=['DELETE'])
def delete_client(id):
    client_repo.delete(id)
    return jsonify({'message': 'Client deleted successfully'}), 204
