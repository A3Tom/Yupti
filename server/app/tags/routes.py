from flask import Blueprint, request, jsonify, make_response
from .models import Tag
from .repository import TagsRepository

tags_repo = TagsRepository()
tags_bp = Blueprint('tags', __name__)

@tags_bp.route('/', methods=['POST'])
def create_tag():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return make_response(jsonify({"error": "Name is required"}), 400)
    
    entity = Tag(**data)
    new_tag = tags_repo.create(entity)

    return jsonify(new_tag.to_dict()), 201


@tags_bp.route('/', methods=['GET'])
def get_tags():
    tags_list = tags_repo.get_all()
    if tags_list is None:
        return jsonify([]), 200
    
    return jsonify([tag.to_dict() for tag in tags_list]), 200


@tags_bp.route('/<int:id>', methods=['GET'])
def get_tag(id):
    tag = tags_repo.get_by_id(id)
    if tag is None:
        return make_response(jsonify({"error": "Tag not found"}), 404)
    
    return jsonify(tag.to_dict()), 200

@tags_bp.route('/<int:id>/timeentries', methods=['GET'])
def get_time_entries_for_tag(id):
    tag = tags_repo.get_by_id_detail(id)
    if tag is None:
        return make_response(jsonify({"error": "Tag not found"}), 404)
    
    time_entries = [time_entry.to_dict() for time_entry in tag.time_entries]
    return jsonify({"name": tag.name, "time_entries": time_entries}), 200


@tags_bp.route('/<int:id>', methods=['PUT'])
def update_tag(id):
    if not tags_repo.exists(id):
        return make_response(jsonify({"error": "Tag not found"}), 404)
    
    tag = tags_repo.update(id, request.get_json())
    return jsonify(tag.to_dict()), 200


@tags_bp.route('/<int:id>', methods=['DELETE'])
def delete_tag(id):
    if not tags_repo.exists(id):
        return make_response(jsonify({"error": "Tag not found"}), 404)
    
    if not tags_repo.delete(id):
        return make_response(jsonify({"error": "Error when deleting tag"}), 400)
    
    return jsonify({'message': 'Tag deleted successfully'}), 200
