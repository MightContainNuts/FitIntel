from sqlalchemy import create_engine
from sqlmodel import SQLModel,Session, select

from services.schemas import SchemaStravaMetaData, settings
from db.models import TabStravaMetaData

class DataBaseHandler:

    def __init__(self, db_url:str = settings.DATABASE_URL):
        self.engine = None
        self.session = None
        self.db = db_url

    def __enter__(self):
        """ setup"""
        self.create_engine()
        self.create_schema()
        self.create_session()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """ teardown """
        if self.session:
            self.session.close()

        if self.engine:
            self.engine.dispose()

        if any((exc_type, exc_val, exc_tb)):
            print(
                f"An error occurred: \n {exc_val} \n {exc_tb} \n {exc_type}")

        print("Database connection closed")



    def create_engine(self):
        """ create db engine to attach to db"""
        self.engine = create_engine(self.db, echo=False)

    def create_session(self):
        """ create db session to attach to db"""
        if self.engine:
            self.session = Session(bind = self.engine)
        else:
            raise ValueError("No db engine configured")

    def create_schema(self):
        """ create db schema to attach to db"""
        if self.engine:
            SQLModel.metadata.create_all(self.engine)
        else:
            raise ValueError("No db engine configured")


    def write_metadata_to_db(self, metadata:SchemaStravaMetaData)->bool:
        """ save metadata to db if not already present """
        if self.engine:
            print("Metadata type:", type(metadata))
            print("Metadata module:",
                  metadata.__class__.__module__)
            if self.check_if_metadata_id_exists(metadata.activity_id):
                print("Already exists")
                return True
            else:
                orm_obj = TabStravaMetaData(**metadata.__dict__)
                self.session.add(orm_obj)
                self.session.commit()
                return True
        return False



    def check_if_metadata_id_exists(self, metadata_id:int)->bool:
        """ check if metadata id exists """
        if self.engine:
            activity = self.session.exec(
                select(TabStravaMetaData).where(TabStravaMetaData.activity_id == metadata_id)).first()
            if activity:
                return True
        return False

