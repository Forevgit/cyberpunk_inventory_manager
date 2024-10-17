from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy.future import select
from inventory import models, schemas
from inventory.inventory_data_service import InventoryDataService

class InventoryService(InventoryDataService):
    def __init__(self, db: Session):
        super().__init__(db)

    async def get_inventory_items(self, skip: int = 0, limit: int = 10) -> List[models.InventoryItem]:
        result = await self.db.execute(select(models.InventoryItem).offset(skip).limit(limit))
        return result.scalars().all()

    async def get_inventory_item(self, item_id: int) -> Optional[models.InventoryItem]:
        result = await self.db.execute(select(models.InventoryItem).where(models.InventoryItem.id == item_id))
        return result.scalars().first()

    async def create_inventory_item(self, item: schemas.InventoryItemCreate):
        db_item = models.InventoryItem(**item.dict())
        return await self.save(db_item)

    async def update_inventory_item(self, item_id: int, item: schemas.InventoryItemUpdate):
        db_item = await self.get_inventory_item(item_id)
        if db_item:
            update_data = item.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_item, key, value)
            await self.db.commit()
            await self.db.refresh(db_item)
            return db_item
        return None

    async def delete_inventory_item(self, item_id: int):
        db_item = await self.get_inventory_item(item_id)
        if db_item:
            await self.delete(db_item)
        return db_item
