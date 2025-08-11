import os
import requests
from pathlib import Path


def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', ".jpg", ".svg", ".jpeg", ".gif"]

    for ext in extensions:
        if ext in image_url:
            return ext


def download_image(image_url: str, name: str, extension: str, folder: str = "images"):
    try:
        filename = f"{name}{extension}"
        os.makedirs(folder, exist_ok=True)
        filepath: Path = Path(os.path.join(folder, filename))

        image_content: bytes = requests.get(image_url).content

        with open(filepath, 'wb') as handler:
            handler.write(image_content)
    except Exception as e:
        print("Error occurred: ", e)

    print("image downloaded successfully...")


if __name__ == "__main__":

    # sample_url_1: str = 'https://w.wallhaven.cc/full/1p/wallhaven-1p398w.jpg'
    # sample_url_2: str = 'https://www.svgrepo.com/show/376344/python.svg'

    url: str = input("Enter an url: ")
    img_name: str = input("Enter a name: ")
    file_ext = get_extension(url)

    print("downloading...")
    download_image(url, img_name, file_ext)



