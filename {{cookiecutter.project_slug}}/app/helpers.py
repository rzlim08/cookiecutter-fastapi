
from fastapi import Depends, Request
from database import AsyncDB, init_async_db, AsyncSession
from settings import Settings
import typing

async def get_settings(request: Request) -> Settings:
    return request.app.state.settings

async def get_engine(
    settings: Settings = Depends(get_settings),
) -> typing.AsyncGenerator[AsyncDB, None]:
    """Wrap resolvers in a DB engine"""
    engine = init_async_db(settings.DB_URI, echo=settings.DB_ECHO)
    try:
        yield engine
    finally:
        pass


async def get_db_session(
    engine: AsyncDB = Depends(get_engine),
) -> typing.AsyncGenerator[AsyncSession, None]:
    """Wrap resolvers in a sqlalchemy-compatible db session"""
    session = engine.session()
    try:
        yield session
    finally:
        await session.close()  # type: ignore