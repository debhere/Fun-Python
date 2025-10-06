import sys
from difflib import get_close_matches
import datetime


def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list[str] = get_close_matches(user_question, questions, n=1, cutoff=0.5)

    if matches:
        return matches[0]


def chat_bot(knowledge: dict):
    while True:
        user_input: str = input("You: ")
        match: str | None = get_best_match(user_input, knowledge)

        if user_input.lower() in ("bye", "exit", "tata"):
            exit_bot()

        if answer := knowledge.get(match):
            print(f"Bot: {answer}")
        else:
            print("Bot: I do not understand...")


def exit_bot():
    sys.exit("Bot: See you...!!")


if __name__ == "__main__":
    brain: dict = {
        "hello": "Hey there!",
        "hi": "Hey there!",
        "how are you": "I am good, thanks",
        "what time is it?": datetime.datetime.now()
    }

    chat_bot(brain)
