from data_access.inventory_data import fetch_inventory, fetch_inventory_item_by_id

class InventoryService:
    def get_inventory(self, warehouse_id=None):
        return fetch_inventory(warehouse_id)

    def get_inventory_item(self, item_id):
        return fetch_inventory_item_by_id(item_id)
