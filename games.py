import random
import sys
from random import sample


class gameFactory:
    def __init__(self, type_of_game):
        self.type_of_game = type_of_game

    def game_category(self):
        if self.type_of_game == "trivia":
            game = input(
                "Enter the type of trivia you want to play: 'Movies' or 'Celebrities' or 'Sports':").lower().strip()
            return triviaFactory(game)
        elif self.type_of_game == "guessing":
            game = input(
                "Enter the type of guessing game you want to play: 'Card' or 'Number' or 'What Am I Riddles':").lower().strip()
            return guessFactory(game)
        elif self.type_of_game == "fill in the blank":
            game = input(
                "Enter the type of fill in the blank game you want to play: 'TV' or 'Math' or 'Music':").lower().strip()
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
            return movie_trivia()
        raise AssertionError("Trivia type is not valid.")


class guessFactory(gameFactory):
    def game_category(self):
        if self.type_of_game == "card":
            return card_guess()
        elif self.type_of_game == "number":
            return number_guess()
        elif self.type_of_game == "what am i riddles":
            return what_am_i_riddles_guess()
        raise AssertionError("Guessing game type is not valid.")


class fibFactory(gameFactory):
    def game_category(self):
        if self.type_of_game == "math":
            return math_fib()
        elif self.type_of_game == "tv":
            return tv_fib()
        elif self.type_of_game == "music":
            return music_fib()
        raise AssertionError("Fill in the blank type is not valid.")


class GameInterface:
    questions = {}

    def check_guess(self):
        score = 0
        for key in self.questions:
            answer = input(f"Question: {key}\nPlease enter you answer: ").lower().strip()
            if answer == self.questions[key]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect")
        return score

    def run_game(self):
        print("You are now starting your game!")
        correct_answers = self.check_guess()
        print(f"You answered {correct_answers} out of 8 correctly! Good job!")


class math_fib(GameInterface):
    questions = {
        "111 + 222 + 333 = ?": "666",
        "200 - (96 / 4) = ?": "176",
        "3 + 6 x (5 + 4) / 3 - 7 = ?": "14",
        "? + 5.13 = 6.45": "1.32",
        "-15 + 22 + ? = 375": "368",
        "150 / (6 + 3 x 8) - 5 = ?": "0",
        "0.61 + 0.81 = ?": "1.42",
        "100 + 423 + ? = 656 ": "133"
    }


class tv_fib(GameInterface):
    questions = {
        "The ______ diaries": "vampire",
        "America's next top ______": "model",
        "The big bang ______": "theory",
        "______ bad": "breaking",
        "Law & order: special victims ______": "unit",
        "The _______ million dollar man": "six",
        "Father knows ______": "best",
        "Are you ______ of the dark?": "afraid"
    }


class music_fib(GameInterface):
    questions = {
        "You ______ with me": "belong",
        "______ yourself": "lose",
        "Love you like a _______": "love song",
        "We are ______": "young",
        "Sweet home _______": "alabama",
        "We found love in a ______": "hopeless place",
        "______ on the water": "smoke",
        "Clap along if you feel like a room without a ______": "roof"
    }


class movie_trivia(GameInterface):
    questions = {
        "For what movie did Tom Hanks score his first Academy Award nomination?": "big",
        "What flavor of Pop Tart does buddy the elf use in his spaghetti in elf?": "chocolate",
        "What hollywood movie star plays himself in Zombieland?": "bill murray",
        "What is the highest-grossing R-rated movie of all time?": "joker",
        "Where were the Lord of the Rings movies filmed?": "new zealand",
        "What is the name of the fictional land where Frozen take place?": "arendelle",
        "What score did Ele Woods get on her LSAT in legally blonde?": "179",
        "What was the top grossing movie of 2014?": "guardians of the galaxy"
    }


class sports_trivia(GameInterface):
    questions = {
        "The olympics are held every how many years?": "4",
        "What sport is best known as the 'king of sports'?": "soccer",
        "What do you call it when a bowler makes 3 strikes in a row?": "turkey",
        "Who has won more tennis grand slam titles, Venus or Serena": "serena",
        "How many holes are played in an average round of golf": "18",
        "In what game is 'love' a score?": "Tennis",
        "In what year were women allowed to compete in the modern Olympic games?": "1990",
        "How many Olympic games were held in countries that no longer exist?": "3"
    }


class celebrities_trivia(GameInterface):
    questions = {
        "Ariana Grande got her start on what kids TV show?": "victorious",
        "Who is the oldest Kardashian sister?": "kourtney",
        "'Blank Space' was a single off of which Taylor Swift album?": "1989",
        "What is the name of Michelle Obama's 2018 memoir?": "becoming",
        "Which artist made history in 2020 as the youngest winner of the Grammys' four main categories?": "Billie Eilish",
        "How many kids does Angelina Jolie have?": "6",
        "What year did Keeping Up with the Kardashian first premier": "2007",
        "Prior to appearing on Parks and Recreation, Rashida Jones starred on what sitcom": "The office"
    }


class what_am_i_riddles_guess(GameInterface):
    questions = {
        "I have a head and a tail that will never meet. Having too many of me is always a treat. What am I?": "coin",
        "I can fly but have no wings. I can cry but have no eyes. Wherever I go, darkness follows me. What am I?": "cloud",
        "I save every day, but my bear stays the sam. What am I?": "barber",
        "I'm where yesterday follow today and tomorrow is in the middle. What am I?": "dictionary",
        "I'm a god, a planet, and I measure heat. What am I?": "mercury",
        "I can never be thrown but I can always be caught. Ways to lose are are always being sought. What am I?": "cold",
        "I have branches, but no fruit, trunk, or leaves. What am I?": "bank",
        "A seed with three letters in my name. Take away two and I still sound the same. What am I?": "pea"
    }


class number_guess(GameInterface):
    def guess_number(self):
        guess = int(input("What number (1-10) do you think I picked?"))
        return guess

    def check_number(self, guess, number):
        if guess > number:
            print("Your guess was too high")
        else:
            print("Your guess was too low")

    def run_game(self):
        number = random.randint(1, 10)
        guess = self.guess_number()
        while guess != number:
            self.check_number(guess, number)
            guess = self.guess_number()
        print(f"You picked {number} which is the correct number!")


class card_guess(GameInterface):
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
