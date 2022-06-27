from flask import Blueprint, render_template
from flask import request
from models import Post, Tag
from app import db
from .forms import PostForm
from flask import redirect
from flask import url_for

posts = Blueprint('posts', __name__, template_folder='templates')


# http://localhost/blog/create
@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        if title != "":
            try:
                post = Post(title=title, body=body)
                db.session.add(post)
                db.session.commit()
            except Exception as e:
                print('Something wrong! ', e)
            return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    q = request.args.get('q')
    if q:
        l_posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
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
