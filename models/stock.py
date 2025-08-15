from modules.db import db

class Stock(db.Model):
    __tablename__ = 'stock'

    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), primary_key=True)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouses.id'), primary_key=True)
    quantity = db.Column(db.Integer)

    inventory = db.relationship('Inventory')
    warehouse = db.relationship('Warehouse')
