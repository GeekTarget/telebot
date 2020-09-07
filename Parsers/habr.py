import requests
from bs4 import BeautifulSoup


def write_id(filename, id):
    with open(filename, 'w') as file:
        file.write(id)


def get_file_id(filename):
    file_id = open(filename).read()
    return file_id


HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
}


def get_main():
    html = requests.get('https://habr.com/ru/all/', headers=HEADERS)
    soup = BeautifulSoup(html.text, 'html.parser')
    post = soup.find('li',
                     class_='content-list__item content-list__item_post shortcuts_item')  # получаем стену из постов
    return post


def get_content():
    post = get_main()
    text = {
        'tittle': post.find('h2', class_='post__title').get_text(strip=True),
        'description': post.find('div', class_='post__body post__body_crop').get_text(
            strip=True),
        'url': post.find('div', class_='post__body post__body_crop').find(
            'a', class_="btn btn_x-large btn_outline_blue post__habracut-btn").get('href')
    }
    post = text['tittle'] + '\n\n' + text['description'] + ' ' + text['url']
    return post


def get_id():
    post = get_main()
    id = post.get('id')  # id поста, который содержится в "post"
    return id

# def defines_new_post():
#     global Id
#     proxies = open('proxy.txt').read().split('\n')
#     useragents = open('user_agent.txt').read().split('\n')
#     while True:
#         proxy = {'http': 'http://' + choice(proxies)}
#         useragent = {'User-Agent': choice(useragents)}
#         if Id == get_id(proxy, useragent):
#             continue
#         else:
#             Id = get_id()
#             return get_content(proxy, useragent)
