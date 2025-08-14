# services/inventory_service.py

from data_access.inventory_data import fetch_inventory, fetch_inventory_item_by_id

def get_inventory_items(warehouse_id=None):
    return fetch_inventory(warehouse_id)

def get_inventory_item_by_id(item_id):
    return fetch_inventory_item_by_id(item_id)
