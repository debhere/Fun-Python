import random

upper, lower = 1, 10
rand_num: int = random.randint(upper, lower)
print(f"Guess the number in the range from {upper} and {lower}")
attempt: int = 3
success: int = 0

while attempt > 0:
    try:
        num = int(input("Guess: "))
    except ValueError as e:
        print("Are you sure you have typed in a number?")
        continue
    finally:
        attempt -= 1
    if num > rand_num:
        print("The number is lower")
    elif num < rand_num:
        print("The number is upper")
    else:
        print("You guessed it")
        success += 1
        break

if attempt == 0 and success == 0:
    print("No more attempts left!")
