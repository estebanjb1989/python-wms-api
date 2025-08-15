# data_access/inventory_data.py

from models.inventory import Inventory
from models.stock import Stock
from app import db

def fetch_inventory(warehouse_id=None):
    query = db.session.query(
        Inventory.id,
        Inventory.name,
        Inventory.packaging,
        Inventory.gtin,
        Stock.warehouse_id,
        Stock.quantity
    ).join(Stock, Inventory.id == Stock.inventory_id)

    if warehouse_id is not None:
        query = query.filter(Stock.warehouse_id == warehouse_id)

    results = query.all()

    # Convert to list of dicts
    return [
        {
            "id": r.id,
            "name": r.name,
            "packaging": r.packaging,
            "gtin": r.gtin,
            "warehouse_id": r.warehouse_id,
            "quantity": r.quantity,
        }
        for r in results
    ]


def fetch_inventory_item_by_id(item_id):
    query = db.session.query(
        Inventory.id,
        Inventory.name,
        Inventory.packaging,
        Inventory.gtin,
        Stock.warehouse_id,
        Stock.quantity
    ).join(Stock, Inventory.id == Stock.inventory_id).filter(Inventory.id == item_id)

    results = query.all()

    if not results:
        return None

    return [
        {
            "id": r.id,
            "name": r.name,
            "packaging": r.packaging,
            "gtin": r.gtin,
            "warehouse_id": r.warehouse_id,
            "quantity": r.quantity,
        }
        for r in results
    ]
