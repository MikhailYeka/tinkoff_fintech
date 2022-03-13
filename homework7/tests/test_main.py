import os
import shutil
from pathlib import Path

from web_scraper.main import main


def test_get_all_urls():
    main(article_number=2, root_url='http://habr.com/')
    cur_dir = Path(os.getcwd()) / Path('habr')
    folder_counter = sum([len(folder) for _, folder, file in os.walk(cur_dir)])
    shutil.rmtree(cur_dir)
    assert folder_counter == 2
