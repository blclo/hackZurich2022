from __future__ import print_function

import datetime
import json
import os.path
from fastapi import Request

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests
import readQR
from floorplan import createFloorplan
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def calendarInfo(data):
    """
    Prints the location of the next event of the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './credentials1.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
           token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the next event')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=1, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next event
        for event in events:
            infoJson = {'floor': 3,
                        'room': 45}

            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event["location"])
            if event["location"] == "":
                return
            info = event["location"].split(", ")
            for i in range(len(info)):
                if info[i].find("floor") == 0:
                    Meetfloor = info[i].split(" ")[1] # takes the number of the floor
                elif info[i].find("room") == 0:
                    meetRoom = info[i].split(" ")[1]


            infoJson = readQR.goMeeting(data, Meetfloor)

            requests.get("http://0.0.0.0:8080/test/"+str(json.dumps(infoJson)))

            pass
    except HttpError as error:
        print('An error occurred: %s' % error)
    createFloorplan(meetRoom)

