from pydantic_settings import BaseSettings
from pydantic import SecretStr
import functools

class Settings(BaseSettings):
    @classmethod
    def load(cls):
        return cls()

    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_USER: str
    DATABASE_PASSWORD: SecretStr
    DATABASE_NAME: str
    DB_ECHO: bool = False

    @functools.cached_property
    def DB_URI(self) -> str:  # noqa: N802
        db_uri = "postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}".format(
            db_host=self.DATABASE_HOST,
            db_port=self.DATABASE_PORT,
            db_user=self.DATABASE_USER,
            db_pass=self.DATABASE_PASSWORD.get_secret_value(),
            db_name=self.DATABASE_NAME,
        )
        return db_uri

    @functools.cached_property
    def SYNC_DB_URI(self) -> str:  # noqa: N802
        db_uri = "postgresql+psycopg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}".format(
            db_host=self.DATABASE_HOST,
            db_port=self.DATABASE_PORT,
            db_user=self.DATABASE_USER,
            db_pass=self.DATABASE_PASSWORD.get_secret_value(),
            db_name=self.DATABASE_NAME,
        )
        return db_uri