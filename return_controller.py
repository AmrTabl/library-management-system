from flask import Blueprint, render_template, request, redirect, session
from models.borrow_record import BorrowRecord
from models.book import Book

return_bp = Blueprint("return", __name__, url_prefix="/return")

@return_bp.route("/", methods=["GET", "POST"])
def return_book():
    if "userid" not in session:
        return redirect("/user/login")

    if request.method == "POST":
        recordID = request.form["recordID"]
        bookID = request.form["bookID"]

        BorrowRecord.return_book(recordID)
        Book.update_status(bookID, "available")

        return redirect("/user/dashboard")

    # show only records belonging to logged-in user
    all_records = BorrowRecord.get_all()
    user_records = [r for r in all_records if r.studentID == session["userid"] and r.returnDate == ""]

    return render_template("return/return.html", records=user_records)
