from flask import Blueprint, render_template, session, redirect
from models.borrow_record import BorrowRecord

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/borrow-records")
def view_borrow_records():
    # Precondition: user must be logged in and admin
    if "userid" not in session or session.get("role") != "admin":
        return redirect("/user/login")

    records = BorrowRecord.get_all()

    return render_template("admin/borrow_records.html", records=records)

from flask import Blueprint, render_template, session, redirect
from models.user import User


@admin_bp.route("/users")
def manage_users():
    # Admin only
    if "userid" not in session or session.get("role") != "admin":
        return redirect("/user/login")

    users = User.get_all()
    return render_template("admin/users.html", users=users)


@admin_bp.route("/users/delete/<userid>")
def delete_user(userid):
    # Admin only
    if "userid" not in session or session.get("role") != "admin":
        return redirect("/user/login")

    User.delete(userid)
    return redirect("/admin/users")