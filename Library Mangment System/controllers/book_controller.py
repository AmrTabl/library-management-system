from flask import Blueprint, render_template, request
from models.book import Book

book_bp = Blueprint("book", __name__, url_prefix="/books")

@book_bp.route("/list")
def list_books():
    books = Book.get_all()
    return render_template("book/list.html", books=books)


@book_bp.route("/search", methods=["GET", "POST"])
def search_books():
    results = []
    if request.method == "POST":
        query = request.form["query"]
        results = Book.search(query)
    return render_template("book/search.html", books=results)
