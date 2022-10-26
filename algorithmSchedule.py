# Chatbot algorithm
# Version 1.0
import random


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
    start_message = input(f"Hi, how can I help you?")
    unsuccessful_attempts = 0
    while start_message:
        type = bot_response(start_message.lower())
        # if user indicates they are trying to schedule an appointment send them to scheduler func
        if type == "yes":
            scheduler()
        # if user is not trying to schedule an appointment get input on what they want to do
        elif type == "no":
            start_message = input()
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
            message = input(f"Enter your message: ")


def scheduler():
    username = input(f"Enter the username of the person you want to schedule an appointment with")
    print(f'Checking {username} calender to see their availability')
    minutes = input(f"How many minutes would you like your meeting to be?")


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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_input_output()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
