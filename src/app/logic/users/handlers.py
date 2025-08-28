class CreateUserCommandHandler:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    async def handle(self, command: CreateUserCommand) -> dict:
        user = UserModel(username=command.username, tg_id=command.tg_id)
        await self.repo.add(user)
        return {status: "success", username: user.username}


class UpdateUserCommandHandler:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    async def handle(self, command: UpdateUserCommand) -> dict:
        user = await self.repo.get_by_id(command.uuid)
        if not user:
            raise BaseException
        if command.username is not None:
            user.username = command.username
        if command.tg_id is not None:
            user.tg_id = command.tg_id
        await self.repo.update(user)
        return {status: "success", username: user.username}


class GetUserByIdQueryHandler:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    async def handle(self, command: GetUserByIdQuery) -> UserResponseDTO:
        user = await self.repo.get_by_id(command.uuid)
        return UserResponseDTO(
            uuid=user.uuid,
            tg_id=user.tg_id,
            username=user.username,
            role=user.role.value,
        )


class GetUserByTgQueryHandler:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    async def handle(self, command: GetUserByTgQuery) -> UserResponseDTO:
        user = await self.repo.get_by_tg(command.tg_id)
        return UserResponseDTO(
            uuid=user.uuid,
            tg_id=user.tg_id,
            username=user.username,
            role=user.role.value,
        )
