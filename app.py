from flask import Flask
from controllers.auth_controller import auth_bp
from controllers.inventory_controller import inventory_bp
from controllers.warehouse_controller import warehouse_bp

def create_app():
    app = Flask(__name__)
    
    # Set a secure secret key (used for JWTs)
    app.config['SECRET_KEY'] = 'your-super-secret-key'  # Replace with environment variable in production

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(warehouse_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)
