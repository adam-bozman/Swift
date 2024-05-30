 
import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///swift_finance.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
