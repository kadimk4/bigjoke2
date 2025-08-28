from abc import abstractmethod


class IUserRepository:
    @abstractmethod
    async def get_by_id(self): ...

    @abstractmethod
    async def get_by_tg(self): ...

    @abstractmethod
    async def add(self): ...

    @abstractmethod
    async def update(self): ...

    @abstractmethod
    async def remove(self): ...
