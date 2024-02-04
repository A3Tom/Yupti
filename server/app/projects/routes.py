from flask import Blueprint, request, jsonify, make_response
from .models import Project

from .repository import ProjectsRepository

projects_repo = ProjectsRepository()
projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/', methods=['POST'])
def create_project():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return make_response(jsonify({"error": "Name is required"}), 400)
    
    entity = Project(**data)
    new_project = projects_repo.create(entity)
    return jsonify(new_project.to_dict()), 201

@projects_bp.route('/', methods=['GET'])
def get_projects():
    projects_list = projects_repo.get_all()
    return jsonify([{'id': project.id, 'name': project.name} for project in projects_list]), 200

@projects_bp.route('/<int:id>', methods=['GET'])
def get_project(id):
    project = projects_repo.get_by_id(id)
    return jsonify({'id': project.id, 'name': project.name}), 200

@projects_bp.route('/<int:id>/detail', methods=['GET'])
def get_project_detail(id):
    project = projects_repo.get_by_id_detail(id)
    return jsonify({'id': project.id, 'name': project.name, 'client': project.client.name}), 200

@projects_bp.route('/<int:id>', methods=['PUT'])
def update_project(id):
    project = projects_repo.update(id, request.get_json())
    return jsonify({'id': project.id, 'name': project.name}), 200

@projects_bp.route('/<int:id>', methods=['DELETE'])
def delete_project(id):
    projects_repo.delete(id)
    return jsonify({'message': 'Project deleted successfully'}), 204
