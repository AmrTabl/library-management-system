from flask import Blueprint, render_template, request, redirect, session
from models.user import User

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        User.register(name, email, password)
        return redirect("/user/login")

    return render_template("user/register.html")


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.validate(email, password)
        if user:
            session["userid"] = user.userid
            session["name"] = user.name
            session["role"] = user.role
            return redirect("/user/dashboard")
        else:
            return "Invalid email or password"

    return render_template("user/login.html")


@user_bp.route("/dashboard")
def dashboard():
    if "userid" not in session:
        return redirect("/user/login")
    return render_template("user/dashboard.html", name=session["name"])


@user_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/user/login")
