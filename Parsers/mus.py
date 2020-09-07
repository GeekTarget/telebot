from bs4 import BeautifulSoup
import requests

global Status
Status = 0

def get_main():
    r = requests.get('https://r.mp3xa.fm/novinki/page/1/')
    soup = BeautifulSoup(r.text,'html.parser')
    music = soup.find('div',class_='plyr-item')
    return music

def get_content():
    music = get_main()
    music_text = {
        'name': music.find('div',class_ = 'name').get_text(),
        'song_name': music.find('div',class_='song_name').get_text(),
        'url' : music.find('div',class_='audio-control').find('a',class_='play').get('data-url')
    }
    text = music_text['name'] + ' - ' + music_text['song_name'] + '\n' + 'Слушать → ' + music_text['url']
    return text

def get_status():
    status = get_main().find('div',class_ = 'name').find('a').get('href')
    return status


