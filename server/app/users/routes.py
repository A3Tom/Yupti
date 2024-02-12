from flask import Blueprint, request, jsonify, make_response
from app.common.cognito_identity_wrapper import CognitoIdentityProviderWrapper
from .models import CreateUserDTO
import boto3
from instance.config import Config

users_bp = Blueprint('users', __name__)

# create a user get route
@users_bp.route('/', methods=['GET'])
def get_users():
    return jsonify({'message': 'Get users route'}), 200

# create a user post route
@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    create_user = CreateUserDTO(**data)

    cog_wrapper = CognitoIdentityProviderWrapper(
        boto3.client("cognito-idp"), Config.AWS_USER_POOL_ID, Config.AWS_APP_CLIENT_ID, Config.AWS_APP_CLIENT_SECRET
    )

    confirmed = cog_wrapper.sign_up_user(
        create_user.username,
        create_user.password, 
        create_user.email,
        )

    # Hawd the bus ! This works, confirmed == False due to needing email verification
    if not confirmed:
        return make_response(jsonify({"error": "Error when creating the user"}), 400)
    
    return jsonify({'message': f'Fuckin Yaldiiiiiiiii, {create_user.name} ya wee bas - yer in!'}), 201