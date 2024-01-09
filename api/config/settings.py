from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    environment: str = "development"

    sqlalchemy_database_url_dev: str
    sqlalchemy_database_url_prod: str
    api_key_dev: str
    api_key_prod: str

    @property
    def sqlalchemy_database_url(self) -> str:
        return (
            self.sqlalchemy_database_url_dev
            if self.environment == "development"
            else self.sqlalchemy_database_url_prod
        )

    @property
    def api_key(self) -> str:
        return (
            self.api_key_dev if self.environment == "development" else self.api_key_prod
        )

    class Config:
        env_file = ".env"


settings = Settings()
