# models/Inventory.py

from modules.db import db

class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    packaging = db.Column(db.String)
    gtin = db.Column(db.String)
