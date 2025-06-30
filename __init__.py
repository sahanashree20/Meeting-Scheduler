from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_cors import CORS

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.Config")

    db.init_app(app)
    mail.init_app(app)
    CORS(app)

    from app import routes, api
    app.register_blueprint(routes.bp)
    app.register_blueprint(api.bp, url_prefix="/api")

    return app
