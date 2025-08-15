# data_access/token_data.py

from app import db
from models.refresh_token import RefreshToken

def add_token(token, username):
    rt = RefreshToken(token=token, username=username)
    db.session.add(rt)
    db.session.commit()

def remove_token(token):
    rt = RefreshToken.query.filter_by(token=token).first()
    if rt:
        db.session.delete(rt)
        db.session.commit()

def is_token_valid(token):
    return RefreshToken.query.filter_by(token=token).first() is not None