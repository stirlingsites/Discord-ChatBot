# Chatbot algorithm working with Discord
# Version 1.0
import random
import datetime


async def bot_response(user_message, ctx) -> str:
    # for each word in user message
    for x in user_message.split():
        # if word is in dictionary key
        if x in dict_input_output.keys():
            # print and return dictionary value for that key
            await ctx.send(f"{dict_input_output[x]}")
            return f"{x}"
    # if key not found return blank string
    return ""


async def user_input_output(ctx, bot):
    await ctx.send("Hi, can I help you?")
    start_message = await bot.wait_for("message", timeout=100)
    unsuccessful_attempts = 0
    while start_message:
        type = await bot_response(start_message.content.lower(), ctx)
        # if user indicates they are trying to schedule an appointment send them to scheduler func
        if type == "yes":
            await scheduler(ctx, bot)
            break
        # if user is not trying to schedule an appointment get input on what they want to do
        elif type == "no":
            start_message = await bot.wait_for("message", timeout=100)
        elif type == "bye":
            # end if user says bye
            break
        # if bot doesn't understand user input
        else:
            await ctx.send(f"Sorry we didn't get that, try rephrasing (enter bye to exit): ")
            start_message = await bot.wait_for("message", timeout=100)
            unsuccessful_attempts += 1
            # send user to real employee in 3 unsuccessful attempts to understand user
            if unsuccessful_attempts == 3:
                await ctx.send("We will transfer you to an associate")
                break


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

dict_input_output = {
    "schedule": "Are you trying to schedule an appointment?",
    "hi": "How can I help you?",
    "hello": "How can I help you?",
    "hey": "How can I help you?",
    "yes": "Ok one moment",
    "no": "What are you trying to do?",
    "goodbye": "ttyl",
    "bye": "ttyl"
}

scheduler_dict = {

}
