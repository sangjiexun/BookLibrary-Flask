# Route definitions for BookLibrary

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from app import app, db
from models import User, Book, Category, BorrowRecord
from forms import LoginForm, RegistrationForm, BookForm, BorrowForm
from datetime import datetime, timedelta

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html', form=form)

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if username already exists
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        # Check if email already exists
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already exists')
            return redirect(url_for('register'))
        
        # Create new user
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Index route
@app.route('/')
@login_required
def index():
    return render_template('index.html')

# Books route
@app.route('/books')
@login_required
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)

# Book detail route
@app.route('/book/<int:id>')
@login_required
def book_detail(id):
    book = Book.query.get_or_404(id)
    return render_template('book_detail.html', book=book)

# Add book route (admin only)
@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.')
        return redirect(url_for('index'))
    
    form = BookForm()
    if form.validate_on_submit():
        # Check if book with ISBN already exists
        if Book.query.filter_by(isbn=form.isbn.data).first():
            flash('Book with this ISBN already exists')
            return redirect(url_for('add_book'))
        
        # Create book
        book = Book(
            title=form.title.data,
            author=form.author.data,
            isbn=form.isbn.data,
            category_id=form.category.data,
            stock=form.stock.data
        )
        db.session.add(book)
        db.session.commit()
        
        flash('Book added successfully!')
        return redirect(url_for('books'))
    
    return render_template('add_book.html', form=form)

# Borrow book route
@app.route('/borrow', methods=['GET', 'POST'])
@login_required
def borrow():
    form = BorrowForm()
    if form.validate_on_submit():
        book = Book.query.get(form.book.data)
        
        # Check if book is available
        if book.stock <= 0:
            flash('Book is not available')
            return redirect(url_for('borrow'))
        
        # Check if user has already borrowed this book
        existing_record = BorrowRecord.query.filter(
            BorrowRecord.user_id == current_user.id,
            BorrowRecord.book_id == book.id,
            BorrowRecord.status == 'borrowed'
        ).first()
        
        if existing_record:
            flash('You have already borrowed this book')
            return redirect(url_for('borrow'))
        
        # Create borrow record
        borrow_record = BorrowRecord(
            user_id=current_user.id,
            book_id=book.id,
            borrow_date=datetime.utcnow().date(),
            due_date=form.due_date.data,
            status='borrowed'
        )
        db.session.add(borrow_record)
        
        # Decrease stock
        book.stock -= 1
        
        db.session.commit()
        
        flash('Book borrowed successfully!')
        return redirect(url_for('index'))
    
    return render_template('borrow.html', form=form)

# Return book route
@app.route('/return/<int:id>', methods=['POST'])
@login_required
def return_book(id):
    borrow_record = BorrowRecord.query.get_or_404(id)
    
    # Check if this is the user's record
    if borrow_record.user_id != current_user.id:
        flash('Access denied. This is not your borrow record.')
        return redirect(url_for('index'))
    
    # Check if book is already returned
    if borrow_record.status == 'returned':
        flash('Book has already been returned')
        return redirect(url_for('index'))
    
    # Update borrow record
    borrow_record.return_date = datetime.utcnow().date()
    borrow_record.status = 'returned'
    
    # Increase stock
    book = Book.query.get(borrow_record.book_id)
    book.stock += 1
    
    db.session.commit()
    
    flash('Book returned successfully!')
    return redirect(url_for('index'))

# User's borrowed books route
@app.route('/my_books')
@login_required
def my_books():
    borrow_records = BorrowRecord.query.filter_by(user_id=current_user.id).all()
    return render_template('my_books.html', borrow_records=borrow_records)

# Admin route
@app.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.')
        return redirect(url_for('index'))
    
    books = Book.query.all()
    users = User.query.all()
    return render_template('admin.html', books=books, users=users)

# Search route
@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        search_type = request.form['search_type']
        
        if search_type == 'title':
            books = Book.query.filter(Book.title.contains(keyword)).all()
        elif search_type == 'author':
            books = Book.query.filter(Book.author.contains(keyword)).all()
        elif search_type == 'isbn':
            books = Book.query.filter(Book.isbn.contains(keyword)).all()
        else:
            books = []
        
        return render_template('search.html', books=books, keyword=keyword, search_type=search_type)
    
    return render_template('search.html')