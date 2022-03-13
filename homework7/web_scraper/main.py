import os
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Generator, List

from web_scraper.get_articles_info import download_url
from web_scraper.get_articles_urls import get_url_from_page
from web_scraper.queues import q


MAX_WORKERS = 20


def get_urls(article_number: int, root_url: str) -> List[str]:
    root_urls = []
    root_urls.append(root_url)
    for page_num in range(2, int(article_number / 20) + 2):
        url = root_url + '/page' + str(page_num)
        root_urls.append(url)
    urls_lists = [url for url in generate_url_list(root_urls, max_work=MAX_WORKERS)]
    urls_list = []
    for urls in urls_lists:
        urls_list.extend(urls)
    urls_list = urls_list[:article_number]
    return urls_list


def make_habr_path() -> Path:
    habr_dir = Path(os.getcwd()) / Path('habr')
    if os.path.exists(habr_dir):
        shutil.rmtree(habr_dir)
    os.mkdir(habr_dir)
    return habr_dir


def main(article_number: int, root_url: str) -> None:
    urls_list = get_urls(article_number=article_number, root_url=root_url)
    habr_dir = make_habr_path()
    for url in urls_list:
        download_url(one_url=url, habr_dir=habr_dir)


def generate_url_list(root_urls: List[str], max_work: int) -> Generator:
    with ThreadPoolExecutor(max_workers=max_work) as executor:
        future_to_url = {
            executor.submit(get_url_from_page, one_url): one_url
            for one_url in root_urls
        }
        for future in as_completed(future_to_url):
            one_url = future_to_url[future]
            try:
                data = future.result()
            except Exception as e:
                print('%r generated an exception: %s' % (one_url, e))
            else:
                yield data
