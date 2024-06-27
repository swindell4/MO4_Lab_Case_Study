from flask import Flask 
from flask import SQLAlchemy 
import json 
app = Flask(__name__) 
app.config[SQLALCHEMY_DATABASE_URI] ="sqlite:///data.db" 
db = SQLAlchemy(app) 
class Book(db.model) 
id = db.Column(db.Integer, primaryKey = True) 
bookName = db.Column(db.String(100), unique = False, nullable = False) 
author = db.Column(db.String(100), unique = False, nullable = False) 
publisher = db.Column(db.String(100), unique = False, nullable = False) 
def __repr__(self): 
   return f"{self.name} - {self.author}"
@app.route ("\Books") 
def getBooks(): 
   books = books.query.all() 
   output = [] 
   for book in books: 
      bookData = {"name":books.bookName, "author":books.author, "publisher":books.publisher} 
      output.append(bookData) 
   return books 
@app.route("\Books\<id>") 
def getBook(id): 
   books = books.query.get_or_404(id) 
   return {"name":book.name, "author":books.author, "publisher": books.publisher} 