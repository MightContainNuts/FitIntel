# pydantic schemas

from pydantic_settings import BaseSettings
from pathlib import Path
from datetime import datetime


class Settings(BaseSettings):
    """env settings"""
    DATABASE_URL: str
    OPENAI_API_KEY: str
    GEMINI_API_KEY: str


    # Strava constants:
    STRAVA_REDIRECT_URI: str = "127.0.0.1"
    STRAVA_CLIENT_SECRET: str
    STRAVA_CLIENT_ID: str
    STRAVA_REFRESH_TOKEN: str



    model_config = {
            "env_file":  str(Path(__file__).parent.parent / ".env"),
            "env_file_encoding": "utf-8",
            "extra":             "ignore",
    }

settings = Settings() # type: ignore

class SchemaStravaMetaData(BaseSettings):
    """ Strava activity metadata"""
    activity_id: int
    activity_name: str
    activity_type: str
    activity_date: datetime