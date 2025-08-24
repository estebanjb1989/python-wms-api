# controllers/auth_controller.py

from flask import Blueprint, request, jsonify
from services import container
from decorators.token_required import token_required 

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
        # return jsonify({"message": "ok"}), 200
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

@auth_bp.route('/me', methods=['GET'])
@token_required
def get_current_user(current_user):
    username = current_user.get("username")
    user = auth_service.find_user_by_username(username)

    if not user:
        return jsonify({"error": "User not found"}), 404

    # Return user info (exclude sensitive data like password)
    return jsonify({
        "id": user.id,
        "username": user.username,
        "role": user.role
    })
