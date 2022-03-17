from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from app.forms import SubscribeForm, CommentForm, BlogForm
from app.models import Subscribe, Post, Comment
from app import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    subscribe = SubscribeForm()
    comment_form = CommentForm()

    if subscribe.validate_on_submit():
        email = request.form.get('email')

        email_exist = Subscribe.query.filter_by(email=email).first()
        if email_exist:
            flash(f'User with email, {email}, is already subscribed to this service.', 'success')
        else:
            new_subscriber = Subscribe(email=email)
            db.session.add(new_subscriber)
            db.session.commit()

            flash('You been successfully subscribed to this service')

        subscribe.email.data = " "

    return render_template('index.html', subscribe = subscribe, form = comment_form)

@views.route('/add_blog', methods=['GET', 'POST'])
@login_required
def add_blog():
    create_blog = BlogForm()

    if create_blog.validate_on_submit:
        post_title = request.form.get('title')
        post_content = request.form.get('text')
        new_blog = Post(post_title=post_title, post_body=post_content, user_id=current_user.id )

        db.session.add(new_blog)
        db.session.commit()

        flash(f'Your blog Post, with title, {post_title}, has been created successfully.', category='success')


    return render_template('create_blog.html', form = create_blog )

@views.route('/add_comment/<post_id>', methods=['POST'])
def add_comment(post_id):
    comment_form = CommentForm()

    if current_user:
        if comment_form.validate_on_submit():
            post_exists = Post.query.filter_by(id=post_id).first()

            if post_exists:
                comment = request.form.get('text')
                new_comment = Comment(comment=comment, post_id=post_id, user_id = current_user.id)
                db.session.add(new_comment)
                db.session.comment()

        else:
            flash('You have Entered Invalid Input')
    
    else:
        flash('You need to be logged in to comment on a post', category='danger')
        return redirect(url_for('auth.login'))

