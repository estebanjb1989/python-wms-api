# data_access/inventory_data.py

from data_connection import get_db_connection

def fetch_inventory(warehouse_id=None):
    query = """
        SELECT p.id, p.name, p.packaging, p.gtin, s.warehouse_id, s.quantity
        FROM products p
        JOIN stock s ON p.id = s.product_id
    """
    params = ()

    if warehouse_id is not None:
        query += " WHERE s.warehouse_id = ?"
        params = (warehouse_id,)

    conn = get_db_connection()
    rows = conn.execute(query, params).fetchall()
    conn.close()

    return [dict(row) for row in rows]

def fetch_inventory_item_by_id(item_id):
    query = """
        SELECT p.id, p.name, p.packaging, p.gtin, s.warehouse_id, s.quantity
        FROM products p
        JOIN stock s ON p.id = s.product_id
        WHERE p.id = ?
    """
    conn = get_db_connection()
    rows = conn.execute(query, (item_id,)).fetchall()
    conn.close()

    return [dict(row) for row in rows]
