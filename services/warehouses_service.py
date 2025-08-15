from data_access.warehouses_data import fetch_all_warehouses

class WarehousesService:
    def get_all(self):
        return fetch_all_warehouses()
