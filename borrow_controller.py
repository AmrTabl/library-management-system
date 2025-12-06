from flask import Blueprint, render_template, request, redirect, session
from models.book import Book
from models.borrow_record import BorrowRecord

borrow_bp = Blueprint("borrow", __name__, url_prefix="/borrow")

@borrow_bp.route("/", methods=["GET", "POST"])
def borrow_book():
    if "userid" not in session:
        return redirect("/user/login")

    if request.method == "POST":
        bookID = request.form["bookID"]
        studentID = session["userid"]

        
        BorrowRecord.create(studentID, bookID)

        
        Book.update_status(bookID, "borrowed")

        return redirect("/user/dashboard")

    books = Book.get_all()
    return render_template("borrow/borrow.html", books=books)

