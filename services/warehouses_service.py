# services/warehouse_service.py

from data_access.warehouses_data import fetch_all_warehouses

def get_all_warehouses():
    return fetch_all_warehouses()
