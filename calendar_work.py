import os
import json
from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauthlib.oauth2.rfc6749.errors import InvalidGrantError

SCOPES = ['https://www.googleapis.com/auth/calendar']


def search_creds(name):
    # Search through the json file to find if the user already has a registered key.
    if os.path.exists('tokens.json'):
        with open('tokens.json', 'r') as tokens:
            data = json.load(tokens)
        if name in data:
            # Write the user's credentials to a json file to be copied to creds.
            with open('token.json', 'w') as token:
                json.dump(data[name], token)
            return Credentials.from_authorized_user_file('token.json', SCOPES)
    # Return None if the user does not have any registered credentials.
    return


async def get_credentials(ctx, bot, embed, author, author2):
    name = author
    creds = search_creds(name)
    author = author2

    if not creds or not creds.valid:
        # Send a request to refresh for the user's credentials if they are expired.
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        # Send a request to ask for the user's credentials if they do not have any registered.
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            flow.redirect_uri = "https://google.com"
            auth_url, _ = flow.authorization_url(prompt='consent')
            embed.description = f"To authorize the bot to access your calendar, sign in [here]({auth_url}) " \
                                "and then respond to this message with the resulting url."

            # TODO: Complete this process through Direct Messages rather than the server channel
            try:
                await author.send(embed=embed)
                response = await bot.wait_for("message", timeout=100)
                code = response.content
                # Slice the url to contain only the authorization code.
                code = code[code.find("code=") + 5:]
                code = code[:code.find('&')]

                # Use the inputted authorization code to fetch the user's token.
                flow.fetch_token(code=code)
                creds = flow.credentials
            except InvalidGrantError:
                await author.send("No valid code was sent. Please try again later.")
                return
            except TimeoutError:
                await author.send("The request timed out. Please try again later.")
                return

        # Write the contents of creds to a json file to be read later.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

        if os.path.exists('tokens.json'):
            with open('tokens.json', 'r') as tokens:
                with open('token.json', 'r') as token:
                    credentials = json.load(token)
                data = json.load(tokens)
            # Overwrite the json file with the updated data dictionary.
            with open('tokens.json', 'w') as tokens:
                # Update the credentials in the json data
                if name in data:
                    data.update({name: credentials})
                else:
                    data[name] = credentials
                json.dump(data, tokens)
        # Create a json if it does not already exist.
        else:
            with open('tokens.json', 'w') as tokens:
                with open('token.json', 'r') as token:
                    credentials = json.load(token)
                data = {name: credentials}
                json.dump(data, tokens)


def search_calendar(author, year, month, day):
    name = author

    start_date = datetime.datetime(year, month, day)
    # Add one day to start_date to create a 24-hour window for events.
    end_date = start_date + datetime.timedelta(days=1)

    # Change the timezone to EST
    start_date = start_date.isoformat() + '-05:00'
    end_date = end_date.isoformat() + '-05:00'

    creds = search_creds(name)

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API.
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMax=end_date, timeMin=start_date,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events.
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)
    except UnboundLocalError:
        print("The username has not been registered to a calendar.")


# Search calendar for Discord bot.
async def search2_calendar(mentions_string, date, mentions_real):
    name = mentions_string

    start_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    # Add one day to start_date to create a 24-hour window for events.
    end_date = start_date + timedelta(days=1)

    # Change the timezone to EST.
    start_date = start_date.isoformat() + '-05:00'
    end_date = end_date.isoformat() + '-05:00'

    creds = search_creds(name)

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API.
        await mentions_real.send('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMax=end_date, timeMin=start_date,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            await mentions_real.send('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events.
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            this_event = event['summary']
            await mentions_real.send(f"{start}, {this_event}")

    except HttpError as error:
        await mentions_real.send('An error occurred: %s' % error)
    except UnboundLocalError:
        await mentions_real.send("The username has not been registered to a calendar.")
    return


def add_event(author, start, end, summary):
    name = author
    creds = search_creds(name)

    start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')

    # Change the timezone to EST.
    start = start.isoformat() + '-05:00'
    end = end.isoformat() + '-05:00'

    # TODO: Change prints to send through Discord
    try:
        service = build('calendar', 'v3', credentials=creds)
        event = {
            'summary': summary,
            'start': start,
            'end': end
        }
        service.events().insert(calendarId='primary', sendNotifications=True, body=event).execute()
    except UnboundLocalError:
        print("You have not registered a calendar to your account. You can start by entering '!calendar'.")


