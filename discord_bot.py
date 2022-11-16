# Chatbot algorithm working with Discord
# Version 1.0
import random
import datetime
import json
import re
import rand_response
import sys


def load_json(file):
    with open(file) as bot_responses:
        print(f"Successfully loaded {file}")
        return json.load(bot_responses)


responses_data = load_json("bot.json")


async def bot_response(user_message, ctx) -> str:
    # for each word in user message
    score_list = []
    message_split = re.split(r'\s+|[,;.?!-]\s*', user_message.lower())
    message_split = [x for x in message_split if not x.startswith('<@')]

    # check each response
    for response in responses_data:
        message_score = 0
        required_score = 0
        required_words = response["required_words"]

        # check if there are required words
        if required_words:
            for word in message_split:
                if word in required_words:
                    required_score += 1

        # check that the number or required words equal to the required score
        if required_score == len(required_words):
            for word in message_split:
                if word in response["user_input"]:
                    message_score += 1
        # add score to list
        score_list.append(message_score)

    # find the best response
    top_response = max(score_list)
    response_index = score_list.index(top_response)

    if user_message == "":
        return "Please enter a message so I can respond!"

    if top_response != 0:
        return responses_data[response_index]["bot_response"]

    return rand_response.random_string()


async def user_input_output(ctx, bot):
    await ctx.send("Hello, you are talking with a scheduling bot. Please enter a message.")
    start_message = await bot.wait_for("message", timeout=100)
    while start_message:
        start_message = start_message.content
        bot_answer = await bot_response(start_message, ctx)
        await ctx.send(bot_answer)
        if bot_answer == "See you later!":
            break
        await ctx.send("Enter another message.")
        start_message = await bot.wait_for("message", timeout=100)


async def scheduler(ctx, bot):
    await ctx.send("Enter the username of the person you want to schedule an appointment with")
    username = await bot.wait_for("message", timeout=100)
    await ctx.send(f'Checking {username.content} calender to see their availability')
    if not await check_date(ctx, bot):
        await ctx.send("Date entered is not valid")
        return
    await ctx.send("How many minutes would you like your meeting to be?")
    minutes = await bot.wait_for("message", timeout=100)
    # TODO check availability of usernames calendar on date for minutes
    await ctx.send(f"{username.content} is available at these time: option 1 option 2 option 3")
    await ctx.send("Please select an option (1, 2, or 3)")
    time_choice = await bot.wait_for("message", timeout=100)
    await ctx.send("What is the requested meeting going to be about?")
    subject = await bot.wait_for("message", timeout=100)
    await ctx.send("Please type any notes you would like to add to the appointment")
    notes = await bot.wait_for("message", timeout=100)
    # TODO create the meeting at time_choice with title subject and any notes
    await ctx.send("Meeting has successfully been created.")
    return 1


async def check_date(ctx, bot):
    await ctx.send("Please enter the year you would like to meet on (YYYY)")
    year = await bot.wait_for("message", timeout=100)
    year = int(year.content)
    await ctx.send("Please enter the month you would like to meet on (MM)")
    month = await bot.wait_for("message", timeout=100)
    month = int(month.content)
    await ctx.send("Please enter the day you would like to meet on (DD)")
    day = await bot.wait_for("message", timeout=100)
    day = int(day.content)
    valid = False
    try:
        new_date = datetime.datetime(year, month, day)
        valid = True
    except ValueError:
        valid = False
    return valid
