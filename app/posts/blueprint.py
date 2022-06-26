from flask import Blueprint, render_template
from models import Post, Tag


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    l_posts = Post.query.all()
    return render_template('posts/index.html', posts=l_posts)


# http://localhost/blog/firs-post
@posts.route('/<slug>')
def post_detail(slug):
    l_post = Post.query.filter(Post.slug == slug).first()
    l_tags = l_post.tags
    return render_template('posts/post_detail.html', post=l_post, tags=l_tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    l_tag = Tag.query.filter(Tag.slug == slug).first()
    l_posts = l_tag.posts.all()
    return render_template('posts/tag_detail.html', tag=l_tag, posts=l_posts)
