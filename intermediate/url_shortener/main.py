import pyshorteners


def short_url(url: str) -> str:
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    return short_url


if __name__ == "__main__":
    try:
        link: str = input("Enter a url: ")
        if link[0].isdigit():
            raise ValueError
        print(f"Here is your short url: {short_url(link)}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
