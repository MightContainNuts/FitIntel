from sqlmodel import SQLModel, Field
from datetime import datetime




class TabStravaMetaData(SQLModel, table=True):
    """db model for strava metadata"""
    activity_id:int = Field(primary_key=True)
    activity_name: str = Field(nullable=False)
    activity_type: str = Field(nullable=False)
    activity_date: datetime = Field(nullable=False)