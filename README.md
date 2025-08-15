pip install Flask-Migrate

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

