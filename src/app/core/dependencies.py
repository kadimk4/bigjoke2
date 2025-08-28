from punq import Container

container = Container()




container.register(async_sessionmaker, instance=AsyncSessionFactory)