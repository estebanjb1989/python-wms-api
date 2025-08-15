from flask import Blueprint, jsonify
from decorators.token_required import token_required
from decorators.role_required import role_required
from services import container

warehouse_bp = Blueprint('warehouse_bp', __name__)
warehouse_service = container.warehouse_service

@warehouse_bp.route('/warehouses', methods=['GET'])
@token_required
@role_required('superadmin')
def get_warehouses(current_user):
    warehouses = warehouse_service.get_all()
    return jsonify([w.to_dict() for w in warehouses]) 
