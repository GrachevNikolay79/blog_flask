from app import app
from app import db

from posts.blueprint import posts

import view


app.register_blueprint(posts, url_prefix='/blog')


def run_app():
    # db.create_all()
    # print('db created?')
    app.run()


if __name__ == '__main__':
    run_app()
