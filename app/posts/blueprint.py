from flask import Blueprint, render_template
from models import Post


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    l_posts = Post.query.all()
    return render_template('posts/index.html', posts=l_posts)


@posts.route('/<slug>')
def post_detail(slug):
    l_post = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/post_detail.html', post=l_post)
