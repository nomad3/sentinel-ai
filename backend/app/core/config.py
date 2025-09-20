from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = Field(default="Sentinel AI")
    VERSION: str = Field(default="0.1.0")

    # Security
    SECRET_KEY: str = Field(default="change-me")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60)

    # CORS
    CORS_ORIGINS: List[str] = Field(default_factory=lambda: [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ])

    # Database
    POSTGRES_HOST: str = Field(default="postgres")
    POSTGRES_PORT: int = Field(default=5432)
    POSTGRES_DB: str = Field(default="sentinel")
    POSTGRES_USER: str = Field(default="sentinel")
    POSTGRES_PASSWORD: str = Field(default="sentinel")

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # ElasticSearch
    ELASTICSEARCH_URL: str = Field(default="http://elasticsearch:9200")

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
    }


settings = Settings()
