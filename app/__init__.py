import os
from flask import Flask;
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import config_options

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():

    app = Flask(__name__)

    # app.config.from_object(config_options['development'])
    app.config['SECRET_KEY'] = '599d43a5cfba1ced86ae18d25da9fc3ef8e9dacbccd3eaa338296ea3a8549cde'
    # Add App Configs
    if app.config['ENV'] == 'development':
        app.config.from_object(config_options['development'])
    elif app.config['ENV'] == 'testing':
        app.config.from_object(config_options['testing'])
    elif app.config['ENV'] == 'production':
        app.config.from_object(config_options['production'])
        URI = os.environ.get('DATABASE_URL')
        if URI and URI.startswith('postgres://'):
            URI = URI.replace('postgres://', 'postgresql://', 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = URI
    else:
        app.config.from_object(config_options['defaultConfig'])

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    from .models import Role, User, Comment, Like, Subscribe

    # Initiliase Database
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprint
    from .main.auth import auth
    from .main.views import views
    app.register_blueprint(auth)
    app.register_blueprint(views)

    # Authenticate User
    login_manager.init_app(app)

    # Load User Session
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    

    return app