from typing import Any

from flask import Flask, request
from web_scraper.main import main
from werkzeug.exceptions import BadRequest

website = 'http://habr.com/ru/all'
app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_number_articles() -> Any:
    try:
        req_data = int(request.get_data())
    except ValueError:
        raise BadRequest
    main(req_data, website)
    return 'OK'

if __name__ == '__main__':
    app.run()
