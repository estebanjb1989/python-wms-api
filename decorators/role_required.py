from functools import wraps
from flask import jsonify

def role_required(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def wrapper(current_user, *args, **kwargs):
            user_role = current_user.get('role', '')
            if user_role not in allowed_roles:
                return jsonify({"error": "Access denied: insufficient permissions"}), 403
            return f(current_user, *args, **kwargs)
        return wrapper
    return decorator


