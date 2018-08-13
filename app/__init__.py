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
    # from app import routes, models
    from app.bucket.routes import bucketlist
    from app.auth.routes import auth_blueprint

    app.register_blueprint(bucketlist)
    app.register_blueprint(auth_blueprint)

    return app
