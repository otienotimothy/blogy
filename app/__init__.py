import os
from flask import Flask;
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config_options

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)

    app.config.from_object(config_options['development'])

    # Add App Configs
    # if app.config['ENV'] == 'development':
    #     app.config.from_object(config_options['development'])
    #     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:moringa@localhost/blogy'
    # elif app.config['ENV'] == 'testing':
    #     app.config.from_object(config_options['testing'])
    # elif app.config['ENV'] == 'production':
    #     app.config.from_object(config_options['production'])
    #     URI = os.environ.get('DATABASE_URL')
    #     if URI and URI.startswith('postgres://'):
    #         URI = URI.replace('postgres://', 'postgresql://', 1)
    #     app.config['SQLALCHEMY_DATABASE_URI'] = URI
    # else:
    #     app.config.from_object(config_options['defaultConfig'])

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    from .models import Role, User, Comment, Like, Subscribe

    # Initiliase Database
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprint
    from .main.auth import auth
    from .main.views import views
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(views)

    

    return app