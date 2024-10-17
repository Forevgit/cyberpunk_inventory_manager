from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from auth import models
from auth import schemas
from database import get_db
from auth.routers import router as auth_router
from inventory.routers import router as inventory_router
app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(inventory_router, prefix="/inventory", tags=["inventory"])

@app.get("/", response_model=list[schemas.UserOut])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User))
    users = result.scalars().all()
    return users