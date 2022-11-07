# Chatbot algorithm
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

def bot_response(user_message) -> str:
    # for each word in user message
    score_list = []
    message_split = re.split(r'\s+|[,;.?!-]\s*', user_message.lower())

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
    return ""


def user_input_output():
    start_message = input(f"Hello, you are talking with a scheduling bot. Please enter a message: ")
    bot_answer = bot_response(start_message)
    print(f"{bot_answer}")
    if bot_answer == "See you later!":
        sys.exit()
    while start_message:
        start_message = input(f"Enter your message: ")


def scheduler():
    username = input(f"Enter the username of the person you want to schedule an appointment with")
    print(f'Checking {username} calender to see their availability')
    if not check_date():
        print("Date entered is not valid")
        return
    minutes = input(f"How many minutes would you like your meeting to be?")
    # TODO check avaliability of usernames calander on date for minutes
    print(f"{username} is avaliable at these time: option 1 option 2 option 3")
    time_choice = input("Please select an option (1, 2, or 3)")
    subject = input("What is the requested meeting going to be about?")
    notes = input("Please type any notes you would like to add to the appointment")
    # TODO create the meeting at time_choice with title subject and any notes
    print("Meeting has successfully been created.")
    return 1


# TODO make date invalid for past
# Checks that Date is valid
def check_date():
    year = int(input(f"Please enter the year you would like to meet on (YYYY)"))
    month = int(input(f"Please enter the month you would like to meet on (MM)"))
    day = int(input(f"Please enter the day you would like to meet on (DD)"))
    dob = input("Please enter dob (dd/mm")
    dob.split()
    valid = False
    try:
        new_date = datetime.datetime(year, month, day)
        valid = True
    except ValueError:
        valid = False
    return valid


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_input_output()
