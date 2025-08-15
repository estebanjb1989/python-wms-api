from flask.cli import FlaskGroup
from app import create_app
from modules.db import db

app = create_app()
cli = FlaskGroup(create_app=lambda: app)

if __name__ == "__main__":
    cli()