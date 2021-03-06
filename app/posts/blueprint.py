from flask import Blueprint, render_template
from flask import request
from models import Post, Tag
from app import db
from .forms import PostForm
from flask import redirect
from flask import url_for

from flask_security import login_required

posts = Blueprint('posts', __name__, template_folder='templates')


# http://localhost/blog/create
@posts.route('/create', methods=['POST', 'GET'])
@login_required
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


@posts.route('/<slug>/edit', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/edit_post.html', post=post, form=form)


@posts.route('/')
def index():
    q = request.args.get('q')
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        l_posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))  # .all()
    else:
        l_posts = Post.query.order_by(Post.id)  # (Post.created.desc()) # .all()

    pages = l_posts.paginate(page=page, per_page=5)
    return render_template('posts/index.html', posts=l_posts, pages=pages)


# http://localhost/blog/firs-post
@posts.route('/<slug>')
def post_detail(slug):
    l_post = Post.query.filter(Post.slug == slug).first_or_404()
    l_tags = l_post.tags
    return render_template('posts/post_detail.html', post=l_post, tags=l_tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    l_tag = Tag.query.filter(Tag.slug == slug).first_or_404()
    l_posts = l_tag.posts.all()
    return render_template('posts/tag_detail.html', tag=l_tag, posts=l_posts)
