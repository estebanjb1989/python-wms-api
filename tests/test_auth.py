# test_auth.py

from services.container import auth_service
from unittest.mock import MagicMock

def test_login_success():
    auth_service.find_user_by_username = MagicMock(return_value={"username": "admin", "password": "123"})
    auth_service.create_access_token = MagicMock(return_value="access123")
    auth_service.create_refresh_token = MagicMock(return_value="refresh456")

    # Simulate request here
