from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from database import get_db
from inventory.service import InventoryService

def get_inventory_service(db: AsyncSession = Depends(get_db)) -> InventoryService:
    return InventoryService(db)
