from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
class SqlUserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session
    
    async def get_by_id(self, user_id: UUID):
        result = await self._session.get()