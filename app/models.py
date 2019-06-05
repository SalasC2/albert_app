from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    wish_list = db.relationship('Book', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)    

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(500), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Book {}>'.format(self.book_name)
    
