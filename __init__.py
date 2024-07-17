from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
    app.config['SECRET_KEY'] = 'secret'


    db.init_app(app)

    with app.app_context():
        from .routes import register_routes
        register_routes(app)
        db.create_all()

    return app