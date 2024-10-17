class InventoryDataService:
    def __init__(self, db_session):
        self.db = db_session

    async def commit(self):
        try:
            await self.db.commit()
        except Exception as e:
            await self.db.rollback()
            raise e

    async def save(self, instance) -> object:
        self.db.add(instance)
        await self.commit()
        await self.db.refresh(instance)
        return instance

    async def delete(self, instance) -> None:
        await self.db.delete(instance)
        await self.commit()