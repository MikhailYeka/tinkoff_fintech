import os
from itertools import count
from pathlib import Path
from typing import List, Tuple

import requests
from bs4 import BeautifulSoup
from requests import Response
from web_scraper.get_articles_urls import get_soup, get_url_for_soup


def get_page_info(url: str) -> Tuple[str, str, List[str]]:
    habr = get_url_for_soup(url)
    soup: BeautifulSoup = get_soup(habr)
    head = str(soup.find('span', class_='post__title-text').text)
    raw_article = soup.find('div', class_='post__text post__text-html post__text_v1')
    article = str(raw_article.text)
    img_url_list = []
    for img_url in raw_article.find_all('img'):
        img_url_list.append(img_url.get('src'))
    return head, article, img_url_list


def download_imgs(img_url_list: List[str], cur_dir: Path) -> None:
    img_num = count()
    for img_url in img_url_list:
        img: Response = requests.get(img_url)
        with open(cur_dir / Path(str(next(img_num))), 'wb') as img_file:
            img_file.write(img.content)


def download_url(one_url: str, habr_dir: Path) -> None:
    head, article, img_url_list = get_page_info(one_url)
    cur_dir = habr_dir / Path(head)
    os.mkdir(cur_dir)
    with open(cur_dir / Path('article.txt'), 'w') as text_file:
        text_file.write(article)
    download_imgs(img_url_list, cur_dir)
