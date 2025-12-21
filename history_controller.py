from flask import Blueprint, render_template, session, redirect
from models.borrow_record import BorrowRecord

history_bp = Blueprint("history", __name__, url_prefix="/history")

@history_bp.route("/")
def view_history():
    # Precondition: student must be logged in
    if "userid" not in session:
        return redirect("/user/login")

    userid = session["userid"]

    records = BorrowRecord.get_by_student(userid)

    return render_template("user/history.html", records=records)
