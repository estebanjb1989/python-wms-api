# data_access/warehouse_data.py
import jsonify

from models.warehouse import Warehouse

def fetch_all_warehouses():
    warehouses = Warehouse.query.all()
    return jsonify([w.to_dict() for w in warehouses])
