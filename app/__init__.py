from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    from app.bucket.views import bucketlist
    # from app.auth.views import auth_blueprint
    from app.auth import auth_blueprint

    app.register_blueprint(bucketlist)
    app.register_blueprint(auth_blueprint)

    return app
