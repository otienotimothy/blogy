from flask import Flask;
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    # Initiliase Database
    db.init_app(app)

    # Register Blueprint
    from main.auth import auth
    from main.views import views
    app.register_blueprint(auth)
    app.register_blueprint(views)

    

    return app