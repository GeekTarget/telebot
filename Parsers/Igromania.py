import requests
from bs4 import BeautifulSoup


def write_url(filename, url):
    with open(filename, 'w') as file:
        file.write(url)


def get_file_url(filename):
    file_url = open(filename).read()
    return file_url


HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}


def get_main():
    html = requests.get('https://www.igromania.ru/news/game/', headers=HEADERS)
    soup = BeautifulSoup(html.text, 'html.parser')
    game_news = soup.find('div', class_='aubl_item')
    return game_news


def get_content():
    news = get_main()
    news_text = {
        'tittle': news.find('div', class_='aubli_data').find('a', class_='aubli_name').get_text(strip=True),
        'description': news.find('div', class_='aubli_data').find('div', class_='aubli_desc').get_text(strip=True)
    }
    text = news_text['tittle'] + '\n' + news_text['description'] + ' Читать дальше → '
    return text


def get_url():
    news = get_main()
    url = 'https://www.igromania.ru/' + news.find('div', class_='aubli_data').find('a', class_='aubli_name').get('href')
    return url
