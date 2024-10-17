from fastapi import APIRouter, Depends, HTTPException
from typing import List

from auth.dependencies import get_current_user
from inventory import schemas
from inventory.service import InventoryService
from inventory.dependencies import get_inventory_service



router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.post("/", response_model=schemas.InventoryItem)
async def create_inventory_item(
    item: schemas.InventoryItemCreate,
    service: InventoryService = Depends(get_inventory_service)
):
    return await service.create_inventory_item(item=item)


@router.get("/", response_model=List[schemas.InventoryItem])
async def read_inventory_items(
    skip: int = 0,
    limit: int = 10,
    service: InventoryService = Depends(get_inventory_service)
):
    return await service.get_inventory_items(skip=skip, limit=limit)


@router.get("/{item_id}", response_model=schemas.InventoryItem)
async def read_inventory_item(
    item_id: int,
    service: InventoryService = Depends(get_inventory_service)
):
    db_item = await service.get_inventory_item(item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.put("/{item_id}", response_model=schemas.InventoryItem)
async def update_inventory_item(
    item_id: int,
    item: schemas.InventoryItemUpdate,
    service: InventoryService = Depends(get_inventory_service)
):
    return await service.update_inventory_item(item_id=item_id, item=item)


@router.patch("/{item_id}", response_model=schemas.InventoryItem)
async def update_inventory_item(
    item_id: int,
    item: schemas.InventoryItemUpdate,
    service: InventoryService = Depends(get_inventory_service)
):
    updated_item = await service.update_inventory_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@router.delete("/{item_id}", response_model=schemas.InventoryItem)
async def delete_inventory_item(
    item_id: int,
    service: InventoryService = Depends(get_inventory_service)
):
    return await service.delete_inventory_item(item_id=item_id)
