from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from model import generateBrochure, translateBrochure


def get_content(url):
    driver = webdriver.Chrome(keep_alive=False)
    driver.get(url)
    time.sleep(2)

    info = driver.page_source

    soup = BeautifulSoup(info, 'html.parser')

    title: str = soup.title.string if soup.title else 'No title found'
    if soup.body:
        for irrelevant in soup.body(['script', 'img', 'input', 'style']):
            irrelevant.decompose()

        text = soup.body.get_text(separator='\n', strip=True)
    else:
        text = ''

    content = (title + '\n\n' + text)[:2000]

    xpath_expr: str = '//body//a[not(ancestor::script) and not(ancestor::img) and not(ancestor::style) and not(ancestor::input)]'
    link_elements = driver.find_elements(by=By.XPATH, value=xpath_expr)

    links: set = set()
    for element in link_elements:
        links.add(element.get_attribute('href'))

    return content, links


if __name__ == "__main__":
    c, l = get_content("https://www.revolut.com")
    brochure = generateBrochure(c, l)
    bengaliBrochure = translateBrochure(brochure, language='bengali')
    print(bengaliBrochure)
