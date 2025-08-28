from msgspec import Struct
from dotenv import load_dotenv
config = load_dotenv()

class DatabaseConfig(Struct):
    user: str = config['DBUser']
    password: str = config['DBPassword']
    address: str = config['DBHost']
    port: str = config['DBPort']
    db: str = config['DBName']
    
    def get_db_url(self):
        return f'postgres+asyncpg://{user}:{password}@{address}:{port}/{db}'

class AppConfig(Struct):
    ...

class RedisConfig(Struct):
    ...

class KafkaConfig(Struct):
    ...

class TelegramConfig(Struct):
    ...

class Config(Struct):
    database: DatabaseConfig = DatabaseConfig()
    app: AppConfig = AppConfig()
    redis: RedisConfig = RedisConfig()
    kafka: KafkaConfig = KafkaConfig()
    telegram: TelegramConfig = TelegramConfig()

settings = Config() # сделать синглтон в DI 