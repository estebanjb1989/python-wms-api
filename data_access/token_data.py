# data_access/token_data.py

from app import db
from models.refresh_token import RefreshToken

def add_token(token, username):
    # Remove any existing token for this username (if your design allows only one per user)
    existing_token = RefreshToken.query.filter_by(username=username).first()
    if existing_token:
        db.session.delete(existing_token)

    # Add new token
    new_token = RefreshToken(token=token, username=username)
    db.session.add(new_token)
    db.session.commit()

def remove_token(token):
    rt = RefreshToken.query.filter_by(token=token).first()
    if rt:
        db.session.delete(rt)
        db.session.commit()

def is_token_valid(token):
    return RefreshToken.query.filter_by(token=token).first() is not None
