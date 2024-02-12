from flask import Blueprint, request, jsonify, make_response
from app.common.cognito_identity_wrapper import CognitoIdentityProviderWrapper

users_bp = Blueprint('users', __name__)

# create a user get route
@users_bp.route('/', methods=['GET'])
def get_users():
    return jsonify({'message': 'Get users route'}), 200

# create a user post route
@users_bp.route('/', methods=['POST'])
def create_user():
    return jsonify({'message': 'Create user route'}), 201