from app import db

class Book(db.Model):
    __tablename__ = 'books'
    bookid =  db.Column(db.Integer,primary_key=True)
    booktitle = db.Column(db.String(50))
    bookauthor = db.Column(db.String(50))