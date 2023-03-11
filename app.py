from flask import Flask

from views import main_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object()
    app.register_blueprint(main_bp)
    return app
