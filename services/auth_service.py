# services/auth_service.py

from data_access.user_data import get_user_by_username
from data_access.token_data import (
    add_token,
    remove_token,
    is_token_valid
)
import jwt
import datetime
from flask import current_app

class AuthService:
    def find_user_by_username(self, username):
        return get_user_by_username(username)

    def create_access_token(self, user):
        payload = {
            "user": user["username"],
            "role": user.get("role", "user"),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
        }
        token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
        return token if isinstance(token, str) else token.decode('utf-8')

    def create_refresh_token(self, user):
        payload = {
            "user": user["username"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
        }
        token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
        token_str = token if isinstance(token, str) else token.decode('utf-8')
        add_token(token_str, user["username"])
        return token_str

    def validate_refresh_token(self, token):
        if not token or not is_token_valid(token):
            return None, "Invalid or expired refresh token"

        try:
            payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            return payload, None
        except jwt.ExpiredSignatureError:
            remove_token(token)
            return None, "Refresh token expired"
        except jwt.InvalidTokenError:
            return None, "Invalid refresh token"

    def invalidate_refresh_token(self, token):
        remove_token(token)
