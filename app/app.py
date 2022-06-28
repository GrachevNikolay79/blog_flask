from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


def create_app():
    l_app = Flask(__name__)
    l_app.config.from_object(Configuration)
    return l_app


app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models import Post, Tag
#admin = Admin(app)
admin = Admin(app, template_mode='bootstrap3')
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))