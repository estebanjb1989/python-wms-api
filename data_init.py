import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

with open('data_schema.sql') as f:
    cursor.executescript(f.read())

# Seed data
cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", 
               ('esteban', '123', 'super admin'))
cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", 
               ('maria', '456', 'warehouse admin'))

products = [
    (301, "Wine Bottle A", "unit", "0123456789012"),
    (302, "Wine Bottle A - Six Pack", "pack of 6", "01234567890129"),
    (303, "Wine Bottle B", "unit", "0987654321098"),
    (304, "Wine Bottle B - Six Pack", "pack of 6", "09876543210985")
]
cursor.executemany("INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?)", products)

warehouses = [
    (1, "Warehouse A", "New York"),
    (2, "Warehouse B", "Los Angeles"),
    (3, "Warehouse C", "Chicago")
]
cursor.executemany("INSERT OR IGNORE INTO warehouses VALUES (?, ?, ?)", warehouses)

stock = [
    (301, 1, 120),
    (302, 1, 20),
    (303, 2, 100),
    (304, 2, 15)
]
cursor.executemany("INSERT INTO stock (product_id, warehouse_id, quantity) VALUES (?, ?, ?)", stock)

conn.commit()
conn.close()
print("Database initialized.")
