from requests import get
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver
import chromedriver_binary
from typing import List


def get_webdriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("window-size=1400,2100")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(chrome_options=chrome_options)


def get_search_results(term: str):
    webdriver = get_webdriver()
    webdriver.get("http://www.google.com/search?q={term}")
    html = webdriver.page_source
    # request = Request(
    #     f"http://www.google.com/search?q={term}", headers={"User-Agent": "Mozilla/5.0"}
    # )
    return html


def parse_results(html: str):
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())
    results: List[Tag] = soup.find_all("a", href=True)
    return [result["href"] for result in results]


if __name__ == "__main__":
    results = get_search_results("ads")
    parse_results(results)
