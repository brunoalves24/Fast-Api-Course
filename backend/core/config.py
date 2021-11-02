import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Settings:
    PROJECT_TITLE: str = "Jobboard"
    PROJECT_VERSION: str = "0.1.0"
    DATABASE_USER : str = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD : str = os.getenv("DATABASE_PASSWORD")
    DATABASE_SERVER : str = os.getenv("DATABASE_SERVER", "localhost")
    DATABASE_PORT : str = os.getenv("DATABASE_PORT", 5432)
    DATABASE_DB : str = os.getenv("DATABASE_DB", "db_course")
    DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_SERVER}:{DATABASE_PORT}/{DATABASE_DB}"

     
settings = Settings()