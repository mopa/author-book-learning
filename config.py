from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str
    LOG_LEVEL: str = "info"

    class Config:
        case_sensitive = True


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
