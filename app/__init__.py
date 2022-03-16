import os
from flask import Flask;
from flask_sqlalchemy import SQLAlchemy
from config import config_options

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

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

    # Initiliase Database
    db.init_app(app)

    # Register Blueprint
    from .main.auth import auth
    from .main.views import views
    app.register_blueprint(auth)
    app.register_blueprint(views)

    

    return app