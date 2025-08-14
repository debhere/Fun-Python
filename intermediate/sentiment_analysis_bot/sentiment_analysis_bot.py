from dataclasses import dataclass
from textblob import TextBlob
import string


@dataclass
class SentimentAnalyzer:
    emoji: str
    indicator: float


def get_sentiment(user_input: str, *, sensitivity: float = 0.4):
    positive_threshold: float = sensitivity
    negative_threshold: float = -sensitivity

    blob = TextBlob(user_input)
    polarity: float = round(blob.polarity, 2)

    if polarity >= positive_threshold:
        feeling = '🙂'
    elif polarity <= negative_threshold:
        feeling = '😟'
    else:
        feeling = '😐'

    return SentimentAnalyzer(feeling, polarity)


def run_bot():
    print("Lia: Welcome! This is Lia Bot. Type something about your day or work and I will do the sentiment analysis")
    print("(press 'q' or type 'exit' to Quit)")

    while True:
        input_text: str = input("Me: ")
        if input_text.lower() == 'q' or input_text.lower() == 'exit':
            print("Lia: Thank you for your participation!")
            break
        elif input_text.isdigit():
            print("Lia: Well! Are you sure you typed in properly? Maybe try again")
            continue
        elif input_text[0] in string.punctuation:
            print("Lia: Well! Are you sure you typed in properly? Maybe try again")
            continue
        else:
            sentiment = get_sentiment(input_text, sensitivity=0.3)
            print(f"Lia: {sentiment.emoji} {sentiment.indicator}")


if __name__ == "__main__":
    run_bot()
