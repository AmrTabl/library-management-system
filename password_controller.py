from flask import Blueprint, render_template, request, redirect
from models.user import User

password_bp = Blueprint("password", __name__, url_prefix="/password")

@password_bp.route("/forgot", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form["email"]

        # Check if email exists
        users = User.get_all()
        for u in users:
            if u.email == email:
                return redirect(f"/password/reset?email={email}")

        return "Email not found"

    return render_template("user/forgot_password.html")


@password_bp.route("/reset", methods=["GET", "POST"])
def reset_password():
    email = request.args.get("email")

    if request.method == "POST":
        new_password = request.form["password"]
        success = User.update_password(email, new_password)

        if success:
            return redirect("/user/login")
        else:
            return "Password reset failed"

    return render_template("user/reset_password.html", email=email)
