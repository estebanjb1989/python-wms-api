# controllers/warehouse_controller.py

from flask import Blueprint, jsonify
from decorators.token_required import token_required
from services.warehouses_service import get_all_warehouses

warehouse_bp = Blueprint('warehouse_bp', __name__)

@warehouse_bp.route('/warehouses', methods=['GET'])
@token_required
def get_warehouses(current_user):
    if current_user['role'] != 'super admin':
        return jsonify({"error": "Access denied: super admin only"}), 403

    warehouses = get_all_warehouses()
    return jsonify(warehouses)
