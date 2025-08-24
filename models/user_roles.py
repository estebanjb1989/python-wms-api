from enum import Enum

class UserRole(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    CREATOR = "creator"
    CONSUMER = "consumer"
