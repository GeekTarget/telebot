import requests

# Constants
TOKEN = 'b4f11915b4f11915b4f11915a9b4829605bb4f1b4f11915ebcfb036062420cb2b10dce2'
HEADERS = {
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
version = '5.122'
domain = 'hdkinoha'

# Нужны для обнаружения новых записей
Date = '1597949100'
date = ''


def write_date(filename, date):
    with open(filename, 'w') as file:
        file.write(str(date))


def get_file_date(filename):
    f = open(filename).read()
    return f


def get_wall(count):
    response = requests.get('https://api.vk.com/method/wall.get', headers=HEADERS,
                            params={'access_token': TOKEN, 'v': version, 'domain': domain, 'count': count})

    data = response.json()['response']['items']
    return data


def get_content():
    global date
    global image
    global url
    count = 1  # диапазон записей от 1
    num = 82371  # нужен для образования ссылки
    if get_wall(count)[0]['is_pinned'] or get_wall(count)[0]['marked_as_ads']:
        """ Проверяет закреплена ли запись или имеет ли рекламу """
        count += 1  # если да, то смотрим следующую запись
        post = get_wall(count)
        if post[1]['marked_as_ads']:
            """ Проверяем является ли запись рекламой """
            count += 1  # если да, то смотрим следующую запись
            num += 1  # изменяем ссылку
            post = get_wall(count)
            text = post[2]['text']
            date = post[2]['date']
            image = post[2]['attachments'][0]['photo']['sizes'][6]['url']
            url = 'https://vk.com/hdkinoha?w=wall-80207939_' + str(num)
            return text
        else:
            num += 1
            text = post[1]['text']
            date = post[1]['date']
            image = post[1]['attachments'][0]['photo']['sizes'][6]['url']
            url = 'https://vk.com/hdkinoha?w=wall-80207939_' + str(num)
            return text
    """ Если 1 запись не закреплена """
    post = get_wall(count)
    num += 1
    text = post[0]['text']
    date = post[0]['date']
    image = post[0]['attachments'][0]['photo']['sizes'][6]['url']
    url = 'https://vk.com/hdkinoha?w=wall-80207939_' + str(num)
    return text

# while True:
#     print('Run')
#     get_content()
#     print(date)
#     print(Date)
#     if Date == date:
#         print('No films')
#         time.sleep(10)
#     else:
#         Date = date
#         print(get_content())
