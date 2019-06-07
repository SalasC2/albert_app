from app import app, db
from app.models import User, Book
from flask import render_template
from flask import request
import requests
import json
from flask import jsonify 

@app.route('/', methods=["GET", "POST"])
def index():
    u = User.query.get(1) 
    if request.method == 'POST':
        if request.form:
            print("TEST")
            result = request.form
            print(result['Name'])
            book  = Book(book_name=result['Name'], author=u)
            db.session.add(book)
            db.session.commit()
            return render_template("profile.html", user=u.username)

    return render_template("index.html", user=u.username)

@app.route('/profile', methods=["GET", "POST"])
def profile():
    u = User.query.get(1)

    return render_template("profile.html", user=u)

@app.route('/delete_book/<book>', methods=["POST", "Delete"])
def delete_book(book):
    u = User.query.get(1)
    b = Book.query.filter_by(book_name=book).delete()
    db.session.commit()
    return render_template("profile.html", user=u)  

# Search By Subject
@app.route('/search_by_subject/<string:subject>', methods=["POST", "GET"])
def search_by_subject(subject):
    r = requests.get('http://openlibrary.org/search.json?subject=%s' % subject)
    data = r.text
    d = json.loads(data)
    return jsonify(d)




