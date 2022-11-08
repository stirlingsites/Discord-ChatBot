import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import calendar_work
import discord_bot
from datetime import datetime
import parsedatetime as pdt

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

cal = pdt.Calendar()
now = datetime.now()


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Setup for sending a date and message from a mention to google calendar and chatbot algorithm respectively
@bot.event
async def on_message(message):
    author = str(message.author)
    if message.author == client.user:
        return
    if message.mentions:
        start_message = message.content
        reply = (f"%s" % (cal.parseDT(str(start_message), now)[0]))
        await calendar_work.search2_calendar(author, message, reply)
        bot_answer = await discord_bot.bot_response(start_message, message)
        await message.channel.send(bot_answer)
        await message.channel.send(reply)


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
