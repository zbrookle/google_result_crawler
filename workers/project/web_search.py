from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver
from typing import List
import chromedriver_binary  # noqa
import random
import time


def fail_chance():
    num = random.randint(1, 100)
    if num <= 20:
        # Random failure
        raise Exception("Failure!")
    if 20 < num <= 40:
        # Temporary network failure
        time.sleep(20)


def get_webdriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("window-size=1400,2100")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(chrome_options=chrome_options)


def get_search_results(term: str):
    fail_chance()
    webdriver = get_webdriver()
    webdriver.get("http://www.google.com/search?q={term}")
    html = webdriver.page_source
    return html


def parse_results(html: str):
    soup = BeautifulSoup(html, features="html.parser")
    results: List[Tag] = soup.find_all("a", href=True)
    return [result["href"] for result in results]
