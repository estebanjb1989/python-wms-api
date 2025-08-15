# data_access/warehouse_data.py
from flask import jsonify

from models.warehouse import Warehouse

def fetch_all_warehouses():
    return Warehouse.query.all()
