from flask import Blueprint, request, jsonify, make_response
from .models import TimeEntry
from .repository import TimeEntriesRepository

time_entries_repo = TimeEntriesRepository()
time_entries_bp = Blueprint('time_entries', __name__)

@time_entries_bp.route('/', methods=['POST'])
def create_time_entry():
    data = request.get_json()    
    entity = TimeEntry(**data)
    new_time_entry = time_entries_repo.create(entity)

    return jsonify(new_time_entry.to_dict()), 201


@time_entries_bp.route('/', methods=['GET'])
def get_time_entrys():
    time_entries_list = time_entries_repo.get_all()
    if time_entries_list is None:
        return jsonify([]), 200
    
    return jsonify([time_entry.to_dict() for time_entry in time_entries_list]), 200


@time_entries_bp.route('/<int:id>', methods=['GET'])
def get_time_entry(id):
    time_entry = time_entries_repo.get_by_id(id)
    if time_entry is None:
        return make_response(jsonify({"error": "Time entry not found"}), 404)
    
    return jsonify(time_entry.to_dict()), 200


@time_entries_bp.route('/<int:id>/detail', methods=['GET'])
def get_time_entry_detail(id):
    time_entry = time_entries_repo.get_by_id_detail(id)
    if time_entry is None:
        return make_response(jsonify({"error": "Time entry not found"}), 404)
    
    return jsonify({'id': time_entry.id, 'description': time_entry.description, 'project': time_entry.project.name, 'client': time_entry.project.client.name}), 200


@time_entries_bp.route('/<int:id>', methods=['PUT'])
def update_time_entry(id):
    if not time_entries_repo.exists(id):
        return make_response(jsonify({"error": "Time entry not found"}), 404)
    
    time_entry = time_entries_repo.update(id, request.get_json())
    return jsonify({'id': time_entry.id, 'name': time_entry.name}), 200


@time_entries_bp.route('/<int:id>', methods=['DELETE'])
def delete_time_entry(id):
    if not time_entries_repo.exists(id):
        return make_response(jsonify({"error": "Time entry not found"}), 404)
    
    if not time_entries_repo.delete(id):
        return make_response(jsonify({"error": "Error when deleting the time entry"}), 400)
    
    return jsonify({'message': 'Time entry deleted successfully'}), 204
