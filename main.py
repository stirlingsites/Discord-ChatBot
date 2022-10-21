import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Command for getting user's credentials for their Google calendar:
"""
    # TODO: Assign username of person calling command to name (change next line)
    name = "John"
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
    if not creds or not creds.valid:
        # Send a request to refresh credentials if they are expired.
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        # Send a request to ask for the user's credentials if the user does not have any registered.
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Write the contents of creds to a json file to be read later.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

        if os.path.exists('tokens.json'):
            with open('tokens.json', 'a+') as tokens:
                with open('token.json', 'r') as token:
                    credentials = json.load(token)
                data = json.load(tokens)
                # Update the credentials in the json data
                if name in data:
                    data.update({name: credentials})
                else:
                    data[name] = credentials
                json.dump(data, tokens)
        # Create json if it does not already exist
        else:
            with open('tokens.json', 'w') as tokens:
                with open('token.json', 'r') as token:
                    credentials = json.load(token)
                data = {name: credentials}
                json.dump(data, tokens)
"""

bot.run(TOKEN)
