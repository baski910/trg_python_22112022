from app import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100))


    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Book.query.all()
