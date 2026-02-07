# Configuration settings for BookLibrary

class Config:
    # Secret key for Flask application
    SECRET_KEY = 'your-secret-key'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask-Login configuration
    LOGIN_DISABLED = False
    
    # Flask-WTF configuration
    WTF_CSRF_ENABLED = True
    
    # Application settings
    APP_NAME = 'Book Library Management System'
    DEBUG = True