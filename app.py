from flask import Flask
from controllers.user_controller import user_bp
from controllers.book_controller import book_bp
from controllers.borrow_controller import borrow_bp
from controllers.return_controller import return_bp
from controllers.history_controller import history_bp
from controllers.admin_controller import admin_bp
from controllers.password_controller import password_bp


def create_app(test_config=None):
    app = Flask(__name__)

    
    app.secret_key = "lms_secret_123"

    if test_config:
        app.config.update(test_config)

    
    app.register_blueprint(user_bp)
    app.register_blueprint(book_bp)
    app.register_blueprint(borrow_bp)
    app.register_blueprint(return_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(password_bp)

    @app.route("/")
    def home():
        return """
        <h1>Welcome to the Library Management System</h1>
        <p><a href='/user/login'>Login</a></p>
        <p><a href='/user/register'>Register</a></p>
        """

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)