from web_scraper.handlers import app

app.testing = True
client = app.test_client()


def test_get_number_articles_400():
    response = client.post('/', data='aa')
    assert response.status_code == 400
