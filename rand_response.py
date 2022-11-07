import random

def random_string():
    random_list = [
        "Please try responding with something more descriptive.",
        "Your wrote something that I cannot understand.",
        "Would you please rephrase that?",
        "I am unable to answer that, please try asking me something else!",
        "I'm sorry, I don't understand what you are asking."
    ]

    list_count = len(random_list)
    randomitem = random.randrange(list_count)

    return random_list[randomitem]