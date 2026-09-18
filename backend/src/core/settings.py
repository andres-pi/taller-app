from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    app_name: str
    app_version: str = "1.0.0"
    app_v1_str: str = "/api/v1"
    app_env: str
    app_debug: bool

    app_port: int

    database_url: str

    #redis_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()