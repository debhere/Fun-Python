import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus


def get_user_agent() -> str:
    agent = UserAgent()
    return agent.chrome


def get_status_description(status_code: int) -> str:
    desc = "??? Unknown status code"
    for status in HTTPStatus:
        if status == status_code:
            desc = status.description
    return desc


def check_website(site: str, user_agent: str):
    try:
        response = requests.get(site, headers={'User-Agent': user_agent})
        print(f"{site} <=> {response}: {get_status_description(response.status_code)}")
    except Exception as e:
        print(f"Could not get information from this website: {site}")


def get_site_list(filepath: str) -> list[str]:
    sites = []
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row[0].startswith("https"):
                row[0] = "https://" + row[0]
            sites.append(row[0])
    return sites


def main():
    agent = get_user_agent()
    websites = get_site_list("sites.csv")

    for website in websites:
        check_website(website, agent)


if __name__ == "__main__":
    main()
