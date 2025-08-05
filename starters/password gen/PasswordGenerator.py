import string
import secrets


def containsUpperCase(passwd: str) -> bool:
    is_exist: bool = False
    for element in passwd:
        if element.isupper():
            is_exist = True
            break
    return is_exist


def containsSymbols(passwd: str) -> bool:
    is_exist: bool = False
    for element in passwd:
        if element in string.punctuation:
            is_exist = True
            break
    return is_exist


def generate_password(length: int, upper=False, special=False) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if upper:
        combination += string.ascii_uppercase
    if special:
        combination += string.punctuation

    new_password = ''
    combination_len = len(combination)

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_len)]

    if (special and not containsSymbols(new_password)) or (upper and not containsUpperCase(new_password)):
        return generate_password(length, upper, special)
    return new_password


if __name__ == "__main__":
    for i in range(1, 6):
        password = generate_password(length=5, upper=True, special=True)
        info = f"Contains Upper: {containsUpperCase(password)}  Contains Special Char: {containsSymbols(password)}"
        print(f"Password {i}: {password}, {info}")
