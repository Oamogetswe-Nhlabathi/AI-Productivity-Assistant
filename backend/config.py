import os
from dotenv import load_dotenv

load_dotenv()

# Flask Configuration
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-change-in-production')

# API Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
AI_PROVIDER = os.getenv('AI_PROVIDER', 'openai')

# Server Configuration
HOST = os.getenv('HOST', 'localhost')
PORT = int(os.getenv('PORT', 5000))

# Database
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///productivity_assistant.db')

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
