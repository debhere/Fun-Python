import random
# This library contains all english words
from english_words import get_english_words_set


def guess_game():
    # First getting the global list of english words, then we only considered the words
    # where the length of the words up to 5 characters
    # we then randomly selected the word from the word list

    globalList = list(get_english_words_set(['web2'], lower=True))
    wordList = [word for word in globalList if len(word) <= 5]
    word: str = random.choice(wordList)

    guessed: str = ''
    attempts: int = 5

    while attempts > 0:
        blanks: int = 0

        print("Word: ", end='')
        for letter in word:
            if letter in guessed:
                print(letter, end='')
            else:
                print('_', end='')
                blanks += 1

        print() # just printing a new line here.

        guess: str = input("Guess a letter: ")

        if blanks == 0 or guess == word:
            print("You win")
            break

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts remaining")
        else:
            guessed += guess

        if attempts == 0:
            print("Better luck next time")
            print(f"The word is: {word}")


if __name__ == "__main__":
    guess_game()
