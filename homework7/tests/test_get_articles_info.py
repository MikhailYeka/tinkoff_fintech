import os
import shutil
from pathlib import Path

from web_scraper.get_articles_info import download_imgs, get_page_info


def test_get_page_info_head(url='https://habr.com/ru/post/100000/'):
    head, _, _ = get_page_info(url)
    assert head == '100k'


def test_get_page_info_article(url='https://habr.com/ru/post/100000/'):
    _, article, _ = get_page_info(url)
    assert len(article) == 306


def test_get_page_info_img(url='https://habr.com/ru/post/100000/'):
    _, _, img_url_list = get_page_info(url)
    assert len(img_url_list) == 0


def test_dowload_imgs():
    cur_dir = Path(os.getcwd()) / Path('test_temp')
    os.mkdir(cur_dir)
    size_before = os.path.getsize(cur_dir)
    img_url_list = [
        'https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Smiley.svg/1200px-Smiley.svg.png'
    ]
    download_imgs(img_url_list=img_url_list, cur_dir=cur_dir)
    size_after = os.path.getsize(cur_dir)
    shutil.rmtree(cur_dir)
    assert size_after > size_before
