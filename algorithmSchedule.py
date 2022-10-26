# Chatbot algorithm
# Version 1.0
import random
import datetime


def bot_response(user_message) -> str:
    # for each word in user message
    for x in user_message.split():
        # if word is in dictionary key
        if x in dict_input_output.keys():
            # print and return dictionary value for that key
            print(f"{dict_input_output[x]}")
            return f"{x}"
    # if key not found return blank string
    return ""


def user_input_output():
    start_message = input(f"Hello, you are talking with a scheduling bot")
    unsuccessful_attempts = 0
    while start_message:
        type = bot_response(start_message.lower())
        # if user indicates they are trying to schedule an appointment send them to scheduler func
        if type == "yes":
            scheduler()
            break
        # if user is not trying to schedule an appointment get input on what they want to do
        elif type == "no":
            start_message = input()
            break
        # if bot doesn't understand user input
        elif type == "":
            message = input(f"Sorry we didn't get that, try rephrasing (enter bye to exit): ")
            unsuccessful_attempts += 1
            # send user to real employee in 3 unsuccessful attempts to understand user
            if unsuccessful_attempts == 3:
                print("We will transfer you to an associate")
                break
        elif type == "bye":
            # end if user says bye
            break
        else:
            start_message = input(f"Enter your message: ")


def scheduler():
    username = input(f"Enter the username of the person you want to schedule an appointment with")
    print(f'Checking {username} calender to see their availability')
    if check_date() == False:
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
    valid = False
    try:
        new_date = datetime.datetime(year, month, day)
        valid = True
    except ValueError:
        valid = False
    return valid


dict_input_output = {
    "schedule": "Are you trying to schedule an appointment?",
    "hi": "Hello, would you like to schedule an appointment?",
    "hello": "Hello, would you like to schedule an appointment?",
    "hey": "Hello, would you like to schedule an appointment?",
    "yes": "Ok one moment",
    "no": "What are you trying to do?",
    "goodbye": "ttyl",
    "bye": "ttyl"
}

scheduler_dict = {

}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_input_output()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
