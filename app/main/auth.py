from flask import Blueprint, flash, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from app.forms import CreateUserForm, LoginForm
from app.models import Role, User
from app import db

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    create_user = CreateUserForm()
    if create_user.validate_on_submit():
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        password_hash = generate_password_hash(password)

        user_exist = User.query.filter_by(email=email).first()
        username_exist = User.query.filter_by(username=username).first()

        if user_exist:
            flash(f'A User with email, {email}, already exists, login instead', category='danger')
        elif username_exist:
            flash(f'The username, {username}, is already being used.', category='danger')
        else:
            user_role = Role.query.filter_by(role='User').first()
            new_user = User(email=email, username=username, password=password_hash, role_id=user_role.id)
            db.session.add(new_user)
            db.session.commit()

            flash('User created successfully', category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.index'))

        create_user.email.data = " "
        create_user.username.data = " "
        create_user.password.data = " "
        create_user.confirm_password.data = " "


    return render_template('signup.html', form = create_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():

    user_login = LoginForm()

    if user_login.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        remember_me = True if request.form.get('remember_me') else False

        user = User.query.filter_by(email=email).first()

        if user:
            password_is_valid = check_password_hash(user.password, password)
            if password_is_valid:
                login_user(user, remember=remember_me)
                return redirect(url_for('views.index'))
            else:
                flash('Invalid Password', category='danger')
        else:
            flash(f'User with Email, {email}, doesn\'t exist, Sign Up.', category='danger')

        user_login.email.data = " "
        user_login.password.data = " "

    return render_template('login.html', form = user_login)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))