from app import app
#from app import db

from posts.blueprint import posts
import view


app.register_blueprint(posts, url_prefix='/blog')


if __name__ == '__main__':
    # db.create_all()
    # print('db created?')
    app.run()

# миграции БД
# flask db init
# flask db migrate
# flask db upgrade
