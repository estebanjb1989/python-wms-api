import json
from pathlib import Path

from app import create_app
from modules.db import db
from models.user import User
from models.warehouse import Warehouse
from models.inventory import Inventory
from models.stock import Stock

DATA_PATH = Path(__file__).parent / "seed_data"

def load_json(filename):
    with open(DATA_PATH / filename, "r") as f:
        return json.load(f)

app = create_app()

with app.app_context():
    # Seed Users
    if not User.query.first():
        users = load_json("users.json")
        user_objs = [User(**user) for user in users]
        db.session.add_all(user_objs)

    # Seed Warehouses
    if not Warehouse.query.first():
        warehouses = load_json("warehouses.json")
        warehouse_objs = [Warehouse(**wh) for wh in warehouses]
        db.session.add_all(warehouse_objs)

    # Seed inventory
    if not Inventory.query.first():
        inventory = load_json("inventory.json")
        inventory_objs = [Inventory(**prod) for prod in inventory]
        db.session.add_all(inventory_objs)

    # Seed Stock
    if not Stock.query.first():
        stock = load_json("stock.json")
        stock_objs = [Stock(**s) for s in stock]
        db.session.add_all(stock_objs)

    db.session.commit()
    print("Seeding completed from JSON files.")
