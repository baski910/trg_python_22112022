import os
from flask_api import FlaskAPI
from flask import request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
#from .models import Book

db = SQLAlchemy()

def create_app():
    from app.models import Book
    app = FlaskAPI(__name__, instance_path=os.getcwd(),instance_relative_config= True)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    db.init_app(app)

    @app.route('/booklists', methods=['GET','POST'])
    def booklists():
        if request.method =='POST':
            title = str(request.data.get('title', ''))
            if title:
                book = Book(title=title)
                book.save()
                response = jsonify(
                    {
                        'id': book.id,
                        'title': book.title
                    }
                )
                response.status_code = 201
                return response
        else:
            booklists = Book.get_all()
            books = []
            for booklist in booklists:
                obj = {
                    'id': booklist.id,
                    'title': booklist.title,
                }
                books.append(obj)
            response = jsonify(books)
            response.status_code = 200
            return response

    return app
