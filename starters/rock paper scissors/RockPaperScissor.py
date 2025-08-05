import random
import sys


class RockPaperScissors:
    def __init__(self):
        print("Welcome to the evergreen game of Rock, Paper and Scissors")
        print("(type 'exit' if you want to quit)")
        print()
        self.actions: dict = {'rock': '💎', 'paper': '🧻', 'scissors': '✂'}
        self.actionList: list = list(self.actions.keys())

    def play_game(self):
        user_input: str = input("Rock, Paper or Scissors? ").lower()

        if user_input == 'exit':
            print("Thanks for playing!")
            sys.exit(1)

        if user_input not in self.actionList:
            print("Check your inputs again")
            return self.play_game()

        ai: str = random.choice(self.actionList)

        self.display(user_input, ai)
        self.validateWinner(user_input, ai)

    @staticmethod
    def validateWinner(usr: str, aiChoice):
        if usr == aiChoice:
            print("It's a tie")
        elif usr == 'rock' and aiChoice == 'scissors':
            print("You win")
        elif usr == 'paper' and aiChoice == 'rock':
            print("You win")
        elif usr == 'scissor' and aiChoice == 'paper':
            print("You win")
        else:
            print("AI wins")

    def display(self, usr, aiChoice):
        print("------")
        print(f"You: {self.actions[usr]}")
        print(f"AI: {self.actions[aiChoice]}")
        print("------")


if __name__ == "__main__":
    rps = RockPaperScissors()

    while True:
        rps.play_game()
