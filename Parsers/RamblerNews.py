import requests
from bs4 import BeautifulSoup


def write_id(id, filename):
    with open(filename, 'w') as file:
        file.write(id)


def get_file_id(filename):
    file_id = open(filename, 'r').read()
    return file_id


HEADERS = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}


def get_main():
    html = requests.get('https://news.rambler.ru/latest/', headers=HEADERS)
    soup = BeautifulSoup(html.text, 'html.parser')
    news = soup.find('div', class_='feed__item')
    return news


def get_content():
    news = get_main()
    text = {
        'tittle': news.find('div', class_="article-summary__title-n-text").find('a',
                                                                                class_='article-summary__title').get_text(
            strip=True),
        'description': news.find('div', class_='article-summary__title-n-text').find('a',
                                                                                     class_='article-summary__text').get_text(
            strip=True),
        'url': 'https://news.rambler.ru' + news.find('div', class_="article-summary__title-n-text").find('a',
                                                                                                         class_='article-summary__title').get(
            'href')
    }
    news_text = text['tittle'] + '\n\n' + text['description'] + ' ' + 'Читать дальше → ' + text['url']
    return news_text


def get_id():
    news = get_main()
    id = news.find('div', class_='article-summary j-article-summary').get('data-clusterid')
    return id

# async def rambler_news_get(proxy, useragent):
#     global Id
#     while True:
#         news_subs = set()
#         for s in base.show_subscribers():
#             if 'Rambler News' in base.show_subs(s[0]):
#                 news_subs.add(s[0])
#         if Id == get_id(proxy, useragent):
#             print('Нет')
#             await asyncio.sleep(uniform(60, 600))
#         else:
#             Id = get_id()
#             for s in news_subs:
#                 await bot.send_message(chat_id=s, text=get_content(proxy, useragent))
