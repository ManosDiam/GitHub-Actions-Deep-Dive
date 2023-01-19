# web_crawler.py

import requests
from bs4 import BeautifulSoup


def count_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")
    return len(links)
