from flask import Flask
from controllers.user_controller import user_bp
from controllers.book_controller import book_bp
from controllers.borrow_controller import borrow_bp
from controllers.return_controller import return_bp

app = Flask(__name__)
app.secret_key = "lms_secret_123"

app.register_blueprint(user_bp)
app.register_blueprint(book_bp)
app.register_blueprint(borrow_bp)
app.register_blueprint(return_bp)


@app.route("/")
def home():
    return """
        <h1>Welcome to the Library Management System</h1>
        <p><a href='/user/login'>Login</a></p>
        <p><a href='/user/register'>Register</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True)

