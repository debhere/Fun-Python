import random


def roll_dice(rolls: int) -> list[int]:
    lower: int = 1
    upper: int = 6
    rolling: list[int] = []

    if rolls <= 1:
        raise ValueError

    for _ in range(rolls):
        output = random.randint(lower, upper)
        rolling.append(output)

    return rolling


def main():
    while True:
        try:
            user_input: str = input("How many dice you like to roll? (type 'exit' to stop the game): ")
            if user_input.lower() == 'exit':
                print("Thanks for playing!")
                break
            no_of_rolls = int(user_input)
            print(*roll_dice(no_of_rolls))
            print(f"sum of rolls: {sum(roll_dice(no_of_rolls))}")
        except ValueError as e:
            print("Please provide a valid input")


if __name__ == "__main__":
    main()
