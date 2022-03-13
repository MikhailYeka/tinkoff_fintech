from typing import List
import time

import requests
from bs4 import BeautifulSoup


def get_url_for_soup(url: str) -> requests.models.Response:
    habr = requests.get(url)
    while habr.status_code == 503:
        time.sleep(1)
        habr = requests.get(url)
    return habr


def get_soup(habr: requests.models.Response) -> BeautifulSoup:
    return BeautifulSoup(habr.text, 'html.parser')


def get_url_from_soup(soup: BeautifulSoup) -> List[str]:
    urls_list = []
    for elem in soup.find_all('h2', class_='post__title'):
        urls_list.append(elem.a.get('href'))
    return urls_list


def get_url_from_page(url: str) -> List[str]:
    habr = get_url_for_soup(url)
    soup = get_soup(habr)
    return get_url_from_soup(soup)
