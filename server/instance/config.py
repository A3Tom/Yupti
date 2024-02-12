from dotenv import load_dotenv
import os

class Config:
    load_dotenv()
    
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'database_uri_not_found')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    
    AWS_USER_POOL_ID = os.getenv('AWS_USER_POOL_ID', 'aws_user_pool_id_not_found')
    AWS_APP_CLIENT_ID = os.getenv('AWS_APP_CLIENT_ID', 'aws_app_client_id_not_found')
    AWS_APP_CLIENT_SECRET = os.getenv('AWS_APP_CLIENT_SECRET', 'aws_app_client_secret_not_found')