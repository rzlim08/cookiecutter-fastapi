""" An example router for FastAPI delete and add your own"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.helpers import get_db_session 
import sqlalchemy as sa
from pydantic import BaseModel, ConfigDict

from app.models.models import Entry as EntryDB


router = APIRouter(
    prefix="/example",
    tags=["example"],
    responses={404: {"description": "Not found"}},
)

class Entry(BaseModel):
    """
    Example model - Delete this model and add your own models
    """
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
    )
    name: str


@router.get("/")
async def get_example(
    session: AsyncSession = Depends(get_db_session),
) -> list[Entry]:
    """
    Get all entries from the leaderboard.
    """
    stmt = sa.select(EntryDB)
    result = await session.execute(stmt)
    entries = result.scalars().all()
    return entries

@router.post("/")
async def add_entry(entry: Entry, session: AsyncSession = Depends(get_db_session)):
    """
    Add a new entry to the leaderboard.
    """
    session.add(EntryDB(
        **entry.model_dump()
    ))
    await session.commit()
    return {"message": "Entry added successfully"}

