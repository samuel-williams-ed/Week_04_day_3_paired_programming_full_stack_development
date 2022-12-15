from flask import render_template, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def tasks():
    books = book_repository.select_all() # NEW
    return render_template("/books/index.html", all_books=books)

@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def destroy(id):
    book_repository.delete(int(id))
    return redirect("/books")