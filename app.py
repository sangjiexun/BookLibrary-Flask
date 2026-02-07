# Main application file for BookLibrary

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import models
from models import User, Book, Category, BorrowRecord

# Import forms
from forms import LoginForm, RegistrationForm, BookForm, BorrowForm

# Import routes
from routes import *

# Login manager callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Main function
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
        
        # Create admin user (if not exists)
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', email='admin@example.com', password='admin123', role='admin')
            db.session.add(admin)
            db.session.commit()
        
        # Create sample categories (if not exists)
        if not Category.query.first():
            categories = [
                Category(name='Fiction', description='Fictional literature'),
                Category(name='Non-Fiction', description='Non-fictional literature'),
                Category(name='Science', description='Science books'),
                Category(name='Technology', description='Technology books'),
                Category(name='History', description='History books')
            ]
            for category in categories:
                db.session.add(category)
            db.session.commit()
        
        # Create sample books (if not exists)
        if not Book.query.first():
            books = [
                Book(title='To Kill a Mockingbird', author='Harper Lee', isbn='978-0-06-112008-4', category_id=1, stock=10),
                Book(title='1984', author='George Orwell', isbn='978-0-452-28423-4', category_id=1, stock=8),
                Book(title='The Great Gatsby', author='F. Scott Fitzgerald', isbn='978-0-7432-7356-5', category_id=1, stock=12),
                Book(title='A Brief History of Time', author='Stephen Hawking', isbn='978-0-553-38016-3', category_id=3, stock=5),
                Book(title='The Selfish Gene', author='Richard Dawkins', isbn='978-0-19-286218-4', category_id=3, stock=7)
            ]
            for book in books:
                db.session.add(book)
            db.session.commit()
    
    app.run(debug=True)