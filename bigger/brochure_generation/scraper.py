from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def get_content(url):
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(keep_alive=False, options=options)
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
