from flask import Blueprint, flash, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import CreateUserForm, LoginForm
from app.models import Role, User
from app import db

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/signup')
def signup():

    create_user = CreateUserForm()

    if create_user.validate_on_submit():
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        password_hash = generate_password_hash(password)

        user_exist = User.query.filter_by(email=email).first()

        if user_exist:
            flash(f'A User with email, {email}, already exists, login instead')
        else:
            user_role = Role.query.filter_by(role='User')
            new_user = User(email=email, username=username, password=password_hash, role_id=user_role.id)
            db.session.add(new_user)
            db.session.commit()

            flash('User created successfully')
            return redirect(url_for('views.index'))


    return render_template('signup.html', form = create_user)

@auth.route('/login')
def login():

    user = LoginForm()

    return render_template('login.html', form = user)


