import os
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_credentials(author):
    name = author
    creds = None

    if os.path.exists('tokens.json'):
        # Search through file to find if the user already has a registered key.
        with open('tokens.json', 'r') as tokens:
            data = json.load(tokens)
            for key in data:
                if key == name:
                    # Write the user's credentials to a json file to be copied to creds.
                    with open('token.json', 'w') as token:
                        json.dump(data[key], token)
                    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
                    break

    # TODO: Ensure requests are visible/appear to the user instead of the bot.
    # TODO: Add timeout feature in case the user decides not to log in or takes too long
    if not creds or not creds.valid:
        # Send a request to ask for the user's credentials if they are expired or the user does not have any registered
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

        # Write the contents of creds to a json file to be read later.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

        if os.path.exists('tokens.json'):
            with open('tokens.json', 'r') as tokens:
                with open('token.json', 'r') as token:
                    credentials = json.load(token)
                data = json.load(tokens)
            # Overwrite the json file with the updated data dictionary
            with open('tokens.json', 'w') as tokens:
                # Update the credentials in the json data
                if name in data:
                    data.update({name: credentials})
                else:
                    data[name] = credentials
                json.dump(data, tokens)
        # Create a json if it does not already exist
        else:
            with open('tokens.json', 'w') as tokens:
                with open('token.json', 'r') as token:
                    credentials = json.load(token)
                data = {name: credentials}
                json.dump(data, tokens)


def search_calendar(author, year, month, day):
    name = author

    start_date = datetime.datetime(year, month, day)
    # Add one day to start_date to create a 24-hour window for events
    end_date = start_date + datetime.timedelta(days=1)

    # Change the timezone to EST
    start_date = start_date.isoformat() + '-05:00'
    end_date = end_date.isoformat() + '-05:00'

    # Get the user's credentials from the json file
    if os.path.exists('tokens.json'):
        with open('tokens.json', 'r') as tokens:
            data = json.load(tokens)
        if name in data:
            with open('token.json', 'w') as token:
                json.dump(data[name], token)
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMax=end_date, timeMin=start_date,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)
    except UnboundLocalError:
        print("The username has not been registered to a calendar.")
