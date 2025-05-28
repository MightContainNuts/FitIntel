# get data back from strava
from datetime import datetime, timedelta

from services.schemas import settings, SchemaStravaMetaData
from services.db_handler import DataBaseHandler
import requests

from typing import Optional, List


class StravaHandler:

    def __init__(self):
        self.data = None
        self.token:Optional[str|None] = None
        self.activities:Optional[List]=None
        self.all_activities:List=[]
        self.activity_metadata:Optional[dict]={}


    def refresh_access_token(self)->None:
        """ TODO:"""
        print("Refreshing access token...")
        URL = "https://www.strava.com/oauth/token"
        PAYLOAD = {
                "client_id": settings.STRAVA_CLIENT_ID,
                "client_secret": settings.STRAVA_CLIENT_SECRET,
                "grant_type": "refresh_token",
                "refresh_token": settings.STRAVA_REFRESH_TOKEN,
                "redirect_uri": settings.STRAVA_REDIRECT_URI,
        }
        now = datetime.now()

        response = requests.post(URL, PAYLOAD)
        if response.status_code == 200:
            print("Successfully refreshed access token...")
            self.token = response.json()["access_token"]
            expires_in = response.json()["expires_in"]
            expiry_time = now + timedelta(seconds=expires_in)
            print(f"Refreshed access token - expires at : {expiry_time.strftime('%d/%m/%Y %H:%M')} ")

        else:
            print("Something went wrong refreshing access token")



    def get_strava_activity_metadata(self, page:int = 1, act_per_page:int=30)->None:
        """ get activities from Strava API"""
        print("Getting activities from Strava API...")
        URL = "https://www.strava.com/api/v3/activities"
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {
                "page": page,
                "per_page": act_per_page,
        }
        response = requests.get(URL, params=params, headers=headers)
        self.activities = response.json()
        for activity in self.activities:

            metadata = SchemaStravaMetaData(
                activity_id=activity["id"],
                activity_name=activity["name"],
                activity_type=activity["type"],
                activity_date=datetime.fromisoformat(
                activity["start_date"].replace("Z",
                                               "+00:00")),
            )
            print(metadata)
            if metadata:
                self.write_metadata_to_db(metadata=metadata)
            else:
                print("Something went wrong getting metadata")


        print(f"Successfully got {len(self.activities)} activities from Strava API")


    @staticmethod
    def write_metadata_to_db(metadata:SchemaStravaMetaData)->None:
        """helper function"""
        success = f"Activity: {metadata.activity_id}: {metadata.activity_name} added to db"
        failure = f"Activity: {metadata.activity_id}: {metadata.activity_name} skipped"
        try:
            with DataBaseHandler() as db:
                result = db.write_metadata_to_db(metadata)
                print(success) if result  else print(failure)

        except Exception as e:
            print(failure, e)



    def get_all_metadata(self):
        """ get all data from Strava API - only needs to be done once"""
        print("Getting ALL data from Strava API...")
        page:int = 1
        act_per_page:int = 100

        while True:
            print(f"Getting ALL data from Strava API page {page} - {act_per_page} per page...")
            self.get_strava_activity_metadata(page, act_per_page)
            self.all_activities += self.activities
            print(f"All Activities now: {len(self.all_activities)} activities!")

            if not self.activities or len(self.activities) < act_per_page:
                print("All Activities complete!")
                break

            page += 1



if __name__ == '__main__':
    s = StravaHandler()
    s.refresh_access_token()
    s.get_all_metadata()


