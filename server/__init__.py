# project/__init__.py


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager


# instantiate the db
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # set up extensions
    login_manager.init_app(app)

    # register blueprints
    from server.api.auth.views import auth_blueprint
    from server.api.profile.views import profile_blueprint
    from server.api.recipe.views import recipe_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(profile_blueprint)
    app.register_blueprint(recipe_blueprint)

    return app
