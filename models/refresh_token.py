# models/refresh_token.py
from modules.db import db

class RefreshToken(db.Model):
    __tablename__ = 'refresh_tokens'

    token = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, db.ForeignKey('users.username'))
