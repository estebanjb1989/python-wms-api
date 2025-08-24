from flask import Flask
from flask_migrate import Migrate
import os
from modules.db import db
from flask_cors import CORS

import config

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Enable CORS
    CORS(app, origins=["http://localhost:3000"])

    # Choose config based on env variable
    env = os.environ.get('FLASK_ENV', 'development').lower()
    if env == 'production':
        app.config.from_object(config.ProductionConfig)
    elif env == 'staging':
        app.config.from_object(config.StagingConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    from controllers.auth_controller import auth_bp
    from controllers.inventory_controller import inventory_bp
    from controllers.warehouse_controller import warehouse_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(warehouse_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=5000)
