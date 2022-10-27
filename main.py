import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import calendar_work
import discord_bot


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Command for getting user's credentials for their Google calendar:
@bot.command(name='calendar')
async def calendar_creds(ctx):
    author = str(ctx.message.author)
    calendar_work.get_credentials(author)


# Command for starting a conversation with the bot
@bot.command(name='chatbot')
async def chatbot(ctx):
    await discord_bot.user_input_output(ctx, bot)


bot.run(TOKEN)
