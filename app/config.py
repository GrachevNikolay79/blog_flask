class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://flask_blog:flask_blog@localhost/blog'
    SECRET_KEY = 'something very secret!'

    SECURITY_PASSWORD_SALT = 'SALT_shugar'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
