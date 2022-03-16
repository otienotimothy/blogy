from flask import Blueprint, flash, render_template, request
from app.forms import SubscribeForm, CommentForm
from app.models import Subscribe
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