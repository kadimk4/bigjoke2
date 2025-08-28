from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from src.app.domain.users.repository import IUserRepository
from sqlalchemy import select

class SqlUserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, user_id: UUID) -> UserModel:
        result = await self._session.get(UserModel, user_id)
        return result
    
    async def get_by_tg(self, tg_id: int) -> UserModel | None:
        result = await self._session.execute(select(UserModel).where(UserModel.tg_id == tg_id))
        return result.scalar_one_or_none

    async def add(self, user: UserModel) -> None:
        await self._session.add(user)
    
    async def update(self, user: UserModel) -> None:
        await self._session.merge(user)
    
    async def remove(self, user: UserModel) -> None:
        await self._session.delete(user)