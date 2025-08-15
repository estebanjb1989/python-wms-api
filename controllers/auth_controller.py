# controllers/auth_controller.py

from flask import Blueprint, request, jsonify
from services import container

auth_bp = Blueprint('auth_bp', __name__)
auth_service = container.auth_service

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = auth_service.find_user_by_username(username)

    if user and user.password == password:
        access_token = auth_service.create_access_token(user)
        refresh_token = auth_service.create_refresh_token(user)
        return jsonify({
            "access_token": access_token,
            "refresh_token": refresh_token
        })
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/refresh', methods=['POST'])
def refresh_token():
    data = request.get_json()
    token = data.get("refresh_token")

    payload, error = auth_service.validate_refresh_token(token)
    if error:
        return jsonify({"error": error}), 401

    new_access_token = auth_service.create_access_token({"username": payload["user"]})
    return jsonify({"access_token": new_access_token})

@auth_bp.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    token = data.get("refresh_token")

    if not token:
        return jsonify({"error": "Refresh token is required"}), 400

    auth_service.invalidate_refresh_token(token)
    return jsonify({"message": "Logged out successfully"})
