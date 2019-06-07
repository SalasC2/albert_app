## SetUp
Create a virtual environment to use using
```python 
python3 -m venv venv
```
Activate virtual enviornment by running 
```python 
source venv/bin/activate
```
To install all dependencies run
```python 
pip install -r requirements.txt
```
Set flask environment variable by using
```bash
export FLASK_APP=albert_app.py
```
Start server using
```python
flask run
```
You should now be able to visit [localhost:5000](localhost:5000)

## Create Database
I'm using SQLAlchemy for my database. There's a users table for users and a Books table to store books, where Users have many books and A book belongs to a user. 

To get things running, you first need to initialize your databse by running
```python
flask db init
```
To get migrations and tables run
```python
flask db upgrade
```

## Routes and Usage

There's a Search by Subject route that gets all books by a certain subject

```
/search_by_subject/<subject>
```

The home page has a form that calls the search by subjcet route and displays all the information on the same page
```
/
```

The second input box allows you to add a book which then redirects you to your profile page

```
/profile
```

From the profile page, you can see a list of books in your wish list and delete them by hitting the remove button next to the book that hits the route to remove the book 

```
/delete_book/<book>
```

## ToDo List

- Want to create a many to many relationship so books can belong to multiple users along with users being able to have many books 
- Instead of an input box to add new books to wishlist, want to have an add button next to each book that adds that book to wishlist. 