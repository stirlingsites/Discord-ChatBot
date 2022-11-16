import sys
from random import sample


class gameFactory:
    def __init__(self, type_of_game):
        self.type_of_game = type_of_game
    def game_category(self):
        if self.type_of_game == "trivia":
            game = input("Enter the type of trivia you want to play: 'Movies' or 'Celebrities' or 'Sports':").lower().strip()
            return triviaFactory(game)
        elif self.type_of_game == "guessing":
            game = input("Enter the type of guessing game you want to play: 'Card' or 'Number' or 'Name':").lower().strip()
            return guessFactory(game)
        elif self.type_of_game == "fill in the blank":
            game = input("Enter the type of fill in the blank game you want to play: 'Riddle' or 'Math' or 'Crossword':").lower().strip()
            return fibFactory(game)
        raise AssertionError("Game type is not valid.")


class triviaFactory(gameFactory):
    def game_category(self):
        print(self.type_of_game)
        if self.type_of_game == "celebrities":
            return celebrities_trivia()
        elif self.type_of_game == "sports":
            return sports_trivia()
        elif self.type_of_game == "movies":
            print("in movie")
            return movie_trivia()
        raise AssertionError("Trivia type is not valid.")

class guessFactory(gameFactory):
    def game_category(self):
        if self.type_of_game == "card":
            return card_guess()
        elif self.type_of_game == "number":
            return number_guess()
        elif self.type_of_game == "person":
            return person_guess()
        raise AssertionError("Guessing game type is not valid.")

class fibFactory(gameFactory):
    def game_category(self):
        if self.type_of_game == "math":
            return math_fib()
        elif self.type_of_game == "riddle":
            return riddle_fib()
        elif self.type_of_game == "crossword":
            return crossword_fib()
        raise AssertionError("Fill in the blank type is not valid.")


class math_fib():
    def hi(self):
        print("math")


class riddle_fib():
    def hi(self):
        print("riddle")


class crossword_fib():
    def hi(self):
        print("crossword")


class movie_trivia():
    def hi(self):
        print("movie")


class sports_trivia():
    def hi(self):
        print("hi")


class celebrities_trivia():
    def hi(self):
        print("celeb")


class person_guess():
    def hi(self):
        print("crossword")


class number_guess():
    def hi(self):
        print("number")


class card_guess():
    # set of possible suits
    suits = {"hearts", "spades", "clubs", "diamonds"}
    # set of possible card values
    values = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', "joker", "queen", "king", "Ace"}

    # states of the machine dictionary
    states = {
        "win": "The computer guessed the correct card!",
        "quit": "You quit the game. Goodbye!",
        "lower": "The correct card value is lower.",
        "higher": "The correct card value is higher",
        "correctsuit": "Computer guessed the correct suit"
    }

    def init(self):
        # Intializes the game and generates the card suit and value for the computer to guess
        print("Welcome to the guess card game!")
        correctsuit = sample(self.suits, 1)[0]
        correctvalue = sample(self.values, 1)[0]
        # Prints the suit and value of the card the computer needs to guess
        print(f"Your cards suit is {correctsuit} and its value is {correctvalue}")
        return "", correctsuit, correctvalue

    # get a suit from the suit set
    def getSuit(self):
        # get the suit to check
        suit = sample(self.suits, 1)[0]
        # create a list of suits that have been checked
        used = {suit}
        while True:
            # ask user if suit is correct
            response = input(f"Is {suit} your suit? Enter 'y' or 'n'. Enter 'quit' to quit")
            # return response based on user input
            if response == "quit":
                print("i quit")
                return None
            elif response == "":
                return None
            elif response in {'y', 'Y'}:
                return "y"
            elif len(used) >= 4:
                # all suits guessed so player is lying
                print("You must have pulled the joker!")
                exit(0)

            # add suit to list if not used
            while True:
                suit = sample(self.suits, 1)[0]
                if suit not in used:
                    used.add(suit)
                    break

    # gets a value from the value set and checks if it is the correct value
    def getValue(self, suit, valueList=values):
        if len(valueList) < 1:
            # Attempted all 14 values so player is lying
            print("You must have the joker!")
            exit(0)

        # gets a value to check if it is the correct value
        value = sample(valueList, 1)[0]
        # asks user if the value is correct
        response = input(f"Is {value} of {suit} your card? Enter 'y' or 'n'. Enter 'quit' to quit")
        # return based on user response
        if response == "quit":
            return None
        if response == "":
            return None
        elif response == "y":
            return response
        else:
            # ask user is the value is higher or lower than correct value
            high_low = input("Is the value higher or lower? Enter 'h' or 'l'. Enter 'quit' to quit.")
            # check if user quits
            if high_low == "quit":
                return None
            if high_low == "":
                return None
            # return if value is higher or lower and the value checked for
            return high_low, value

    def update(self, gamestate, guessedsuit, guessedvalue="n"):
        """
        Update game state

        :param gamestate: state of the game
        :param correctnum: magic number to find
        :param guess: player's guess
        :return: the state
        """
        # check for conditions that would change gamestate and set gamestate if true
        if guessedsuit is None:
            gamestate = "quit"
        elif guessedsuit == "y":
            gamestate = "correctsuit"
        elif guessedvalue is None:
            gamestate = "quit"
        elif guessedvalue == 'h':
            gamestate = "higher"
        elif guessedvalue == 'l':
            gamestate = "lower"
        elif guessedvalue == 'y':
            gamestate = "win"

        return gamestate

    # update gamestate
    def render(self, gamestate):
        if gamestate in self.states:
            print(self.states[gamestate])
        else:
            raise RuntimeError("Unexpected state {}".format(gamestate))

    def run_game(self):
        # initate the starting values
        gamestate, correctsuit, correctvalue = self.init()
        # run getSuit function to find correct suit
        guessedsuit = self.getSuit()
        # update gamestate after finding suit
        gamestate = self.update(gamestate, guessedsuit)
        self.render(gamestate)
        while gamestate != "win" and gamestate != "quit":
            # run getVlue function to find correct value
            guessedvalue = self.getValue(correctsuit)
            # update gamestate
            gamestate = self.update(gamestate, correctsuit, guessedvalue[0])
            self.render(gamestate)
            # if the gamestate is higher than remove values to check lower than or same as value checked for
            if gamestate == "higher":
                temp = self.values.copy()
                for v in temp:
                    if v.zfill(2) <= guessedvalue[1].zfill(2):
                        self.values.remove(v)
            # if the gamesate is lower than remove value to check for higher or same as value checked for
            elif gamestate == "lower":
                temp = self.values.copy()
                for v in temp:
                    if v.zfill(2) >= guessedvalue[1].zfill(2):
                        self.values.remove(v)
        sys.exit()

"""# user picks game they want to play
game_choice = input("Enter the type of game you want to play: 'Trivia' or 'Guessing' or 'Fill in the Blank':").lower().strip()
# send users choice to game factory
gametype = gameFactory(game_choice)
# calls game_category function on object to determine type of game user wants to play
result = gametype.game_category()
# calls game_category function on object to determine category of chosen game  user wants to play
type = result.game_category()
# run the game the user picked
type.run_game()
"""