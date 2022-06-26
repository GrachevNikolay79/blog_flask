from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate


def create_app():
    l_app = Flask(__name__)
    l_app.config.from_object(Configuration)
    return l_app


app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
