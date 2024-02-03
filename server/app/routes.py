from flask import request, jsonify, abort
from app.models import Client, Project#, TimeEntry
from run import app, db

# # Create a new time entry
# @app.route('/time_entries', methods=['POST'])
# def add_time_entry():
#     data = request.json
#     try:
#         dto = TimeEntry(**data)
#     except TypeError as e:
#         return jsonify({'error': str(e)}), 400

#     new_entry = TimeEntry(
#         project_id=dto.project_id, 
#         start_time=dto.start_time, 
#         end_time=dto.end_time, 
#         description=dto.description
#     )
#     db.session.add(new_entry)
#     db.session.commit()
#     return jsonify({'message': 'New time entry added'}), 201

# # Get all time entries
# @app.route('/time_entries', methods=['GET'])
# def get_time_entries():
#     entries = TimeEntry.query.all()
#     return jsonify([entry.to_dict() for entry in entries]), 200

# # Update a time entry
# @app.route('/time_entries/<int:id>', methods=['PUT'])
# def update_time_entry(id):
#     entry = TimeEntry.query.get_or_404(id)
#     data = request.json
#     try:
#         dto = TimeEntry(**data)
#     except TypeError as e:
#         return jsonify({'error': str(e)}), 400

#     entry.project_id = dto.project_id
#     entry.start_time = dto.start_time
#     entry.end_time = dto.end_time
#     entry.description = dto.description
#     db.session.commit()
#     return jsonify({'message': 'Time entry updated'}), 200

# # Delete a time entry
# @app.route('/time_entries/<int:id>', methods=['DELETE'])
# def delete_time_entry(id):
#     entry = TimeEntry.query.get_or_404(id)
#     db.session.delete(entry)
#     db.session.commit()
#     return jsonify({'message': 'Time entry deleted'}), 200



@app.route('/clients', methods=['GET'])
def get_clients():
    clients = db.session.query(Client).all()
    return jsonify([ client.to_dict() for client in clients]), 200

@app.route('/projects', methods=['GET'])
def get_projects():
    projects = db.session.query(Project).all()
    return jsonify([ project.to_dict() for project in projects]), 200

@app.route('/joins', methods=['GET'])
def get_join():
    projects = db.session.query(Project).join(Project.client).all()
    return jsonify([ project.to_dict() for project in projects]), 200
