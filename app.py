# app.py
from flask import Flask
from modules.db import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate = Migrate(app, db)

    print(migrate)

    with app.app_context():
        db.create_all()

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
