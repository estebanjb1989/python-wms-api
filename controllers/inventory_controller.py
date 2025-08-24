# controllers/inventory_controller.py

from flask import Blueprint, jsonify, request
from decorators.token_required import token_required 
from services import container

inventory_bp = Blueprint('inventory_bp', __name__)
inventory_service = container.inventory_service

@inventory_bp.route('/inventory', methods=['GET'])
@token_required
def get_inventory():
    warehouse_id = request.args.get('warehouse_id')

    if warehouse_id:
        try:
            warehouse_id = int(warehouse_id)
        except ValueError:
            return jsonify({"error": "warehouse_id must be an integer"}), 400
    else:
        warehouse_id = None

    inventory = inventory_service.get_inventory_items(warehouse_id)
    return jsonify(inventory)

@inventory_bp.route('/inventory/<int:item_id>', methods=['GET'])
@token_required
def get_inventory_item(current_user, item_id):
    rows = inventory_service.get_inventory_item_by_id(item_id)

    if not rows:
        return jsonify({"error": "Inventory item not found"}), 404

    return jsonify(rows if len(rows) > 1 else rows[0])
