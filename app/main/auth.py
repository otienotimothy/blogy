from flask import Blueprint, render_template
from app.forms import CreateUserForm, LoginForm

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/signup')
def signup():

    create_user = CreateUserForm()

    return render_template('signup.html', form = create_user)

@auth.route('/login')
def login():

    user = LoginForm()

    return render_template('login.html', form = user)


