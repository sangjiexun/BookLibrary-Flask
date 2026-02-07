# Form definitions for BookLibrary

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, TextAreaField, DateField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from models import Category, Book

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=100)])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=50)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=100)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class BookForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(max=200)])
    author = StringField('Author', validators=[InputRequired(), Length(max=100)])
    isbn = StringField('ISBN', validators=[InputRequired(), Length(max=20)])
    category = SelectField('Category', coerce=int, validators=[InputRequired()])
    stock = IntegerField('Stock', validators=[InputRequired()])
    submit = SubmitField('Submit')
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name) for category in Category.query.all()]

class BorrowForm(FlaskForm):
    book = SelectField('Book', coerce=int, validators=[InputRequired()])
    due_date = DateField('Due Date', validators=[InputRequired()])
    submit = SubmitField('Borrow')
    
    def __init__(self, *args, **kwargs):
        super(BorrowForm, self).__init__(*args, **kwargs)
        # Only show books with stock > 0
        self.book.choices = [(book.id, f'{book.title} by {book.author}') for book in Book.query.filter_by(stock__gt=0).all()]