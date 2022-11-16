# Chatbot algorithm
# Version 1.0
import json
import re
import rand_response
import sys
import games

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
        list_length = len(responses_data[response_index]["bot_response"])
        return responses_data[response_index]["bot_response"]

    return rand_response.random_string()
    return ""


def user_input_output():
    start_message = "Hello, you are using the scheduling bot."
    print(start_message)
    while start_message:


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_input_output()
