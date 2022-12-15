from db.run_sql import run_sql

import repositories.author_repository as author_repository
from models.book import Book

def save(book):
    sql = "INSERT INTO books (title, author_id) VALUES (%s, %s) RETURNING * "
    values = [book.title, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def view_all():
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    books = []
    for book in results:
        author_id = book['author_id']
        author = author_repository.select(author_id)
        created_book = Book(book['title'], author, book['id'])
        books.append(created_book)
    return books

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    #find each book (row) from db
    for row in results:

        #get the author object from other database
        author_id = row['author_id']
        author = author_repository.select(author_id) 

        #need to insert an author object
        book = Book(row['title'], author, row['id'] )

        # debugging print statments
        print("")
        print(book.__dict__)
        
        books.append(book)
    return books

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

