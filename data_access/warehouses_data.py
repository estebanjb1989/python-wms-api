# data_access/warehouse_data.py

from data_connection import get_db_connection

def fetch_all_warehouses():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM warehouses").fetchall()
    conn.close()
    return [dict(row) for row in rows]
