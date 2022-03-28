import os 


class Settings:

    PROJECT_NAME: str = "UPLOAD CSV TO DATABASE"
    PROJECT_VERSION: str = "1.0.0"

    # SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_DATABASE_URL = "sqlite:///./csv_app.db"



settings = Settings()

SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL




