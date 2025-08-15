# services/container.py

from services.auth_service import AuthService
from services.inventory_service import InventoryService
from services.warehouses_service import WarehousesService

auth_service = AuthService()
inventory_service = InventoryService()
warehouse_service = WarehousesService()
