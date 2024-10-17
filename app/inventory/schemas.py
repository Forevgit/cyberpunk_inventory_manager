from pydantic import BaseModel,ConfigDict
from typing import  Optional

class InventoryItemBase(BaseModel):
    name: str
    description: str
    category: str
    quantity: int
    price: float

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None

class InventoryItem(InventoryItemBase):
    id: int
    model_config = ConfigDict(orm_mode=True)
