# modules needed
# flask
# flask-sqlalchemy
# flask-migrate

# commands used for migrating
# flask db init  - migrations
# flask db migrate - migrations/version/*.py
# flask db upgrade - create tables inside database
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

def create_app():
    from .models import Book
    app = Flask(__name__,instance_path= os.getcwd(),instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app,db)

    @app.route('/books')
    def books():
        objects = Book.query.all()
        books = []
        for obj in objects:
            d1 = {}
            d1['bookid'] = obj.bookid
            d1['booktitle'] = obj.booktitle
            d1['bookauthor'] = obj.bookauthor
            books.append(d1)
        return render_template("books.html",books = books)

    @app.route('/addbooks', methods = ['GET','POST'])
    def addbooks():
        if request.method == 'POST':
            booktitle = request.form['booktitle']
            bookauthor = request.form['bookauthor']
            book = Book(booktitle = booktitle, bookauthor= bookauthor)
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('books'))
        else:
            return render_template("addbooks.html")
    return app