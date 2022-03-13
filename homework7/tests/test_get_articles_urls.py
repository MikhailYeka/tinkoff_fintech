import bs4
from web_scraper.get_articles_urls import get_soup, get_url_from_soup, get_url_for_soup


def test_get_soup():
    url = 'https://habr.com/ru/post/100000/'
    habr = get_url_for_soup(url)
    soup = get_soup(habr)
    assert soup.title.text == '100k / Хабр'
    assert isinstance(soup, bs4.BeautifulSoup)


def test_get_url_from_soup():
    with open('tests/habr_for_test.html', 'r') as f:
        html_doc = f.read()
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    urls_list = get_url_from_soup(soup)
    assert len(urls_list) == 20

