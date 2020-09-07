import asyncio
from random import uniform

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

import config
from Datebase import DateBase
from Parsers import RamblerNews, Igromania, habr, NewFilmVK, mus
from main import dp, bot
from Keyboard import keyboards

base = DateBase('base.db')


# Function for keyboard "Подписаться"
@dp.message_handler(Command('subscribe'))
async def get_inline_btn(message: types.Message):
    await message.answer('Выберите подписку или нажмите кнопку отмены:', reply_markup=keyboards.subscriptions)


@dp.callback_query_handler(text_contains='True')
async def subscribe(call: CallbackQuery):
    await call.answer(cache_time=60)
    data = call.data  # Название
    d = data.split(':')  # подписки
    base.subscribe(call.message.chat.id, d[1])
    await call.message.edit_reply_markup()
    await call.message.answer(base.message)


# Function for keyboard "cancel"
@dp.callback_query_handler(text='cancel')
async def not_subscribe(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.answer('Действие отменено.')


# Function for command "Отписка"
@dp.message_handler(Command('unsubscribe'))
async def get_inline_btn(message: types.Message):
    await message.answer('Выберите отписку или нажмите кнопку отмены:', reply_markup=keyboards.unsubscriptions)


@dp.callback_query_handler(text_contains='False')
async def unsubscribe(call: CallbackQuery):
    await call.answer(cache_time=60)
    data = call.data
    d = data.split(':')
    base.unsubscribe(call.message.chat.id, d[1])
    await call.message.edit_reply_markup()
    await call.message.answer(base.message)


# Function for command "Подписки"
@dp.message_handler(Command('subscriptions'))
async def get_subscriptions(message: types.Message):
    await message.answer('У вас активны следующие подписки: ' + str(base.show_subs(message.chat.id)))


# Function for command "help"
@dp.message_handler(Command('help'))
async def get_information(message: types.Message):
    text = config.text
    await message.answer(text)


# Function for News mailing
async def rambler_news_get():
    while True:
        try:
            news_subs = set()
            for s in base.show_subscribers():
                if 'News📝' in base.show_subs(s[0]):
                    news_subs.add(s[0])
            id = RamblerNews.get_id()
            if RamblerNews.get_file_id('news.txt') == id:
                await asyncio.sleep(uniform(60, 300))
            else:
                RamblerNews.write_id(id, 'news.txt')
                # RamblerNews.Id = RamblerNews.get_id()
                for s in news_subs:
                    await bot.send_message(chat_id=s, text=RamblerNews.get_content())
        except:
            print('Error')
            await asyncio.sleep(1800)


# Function for Game mailing
async def igromania_get():
    while True:
        try:
            game_subs = set()
            for s in base.show_subscribers():
                if 'Games🎮' in base.show_subs(s[0]):
                    game_subs.add(s[0])
            url = Igromania.get_url()
            if Igromania.get_file_url('igromania.txt') == url:
                await asyncio.sleep(uniform(600, 800))
            else:
                Igromania.write_url('igromania.txt', url)
                for s in game_subs:
                    await bot.send_message(chat_id=s, text=Igromania.get_content() + Igromania.get_url())
        except:
            print('Error')
            await asyncio.sleep(1800)


# Function for Habr mailing
async def habr_get():
    while True:
        try:
            habr_subs = set()
            for s in base.show_subscribers():
                if 'Habr-IT blog👨‍💻' in base.show_subs(s[0]):
                    habr_subs.add(s[0])
            id = habr.get_id()
            if habr.get_file_id('habr.txt') == id:
                await asyncio.sleep(uniform(400, 600))
            else:
                habr.write_id('habr.txt', id)
                for s in habr_subs:
                    await bot.send_message(chat_id=s, text=habr.get_content())
        except:
            print('Error')
            await asyncio.sleep(1800)

# Function for Film mailing
async def new_film_get():
    while True:
        try:
            films_sub = set()
            for s in base.show_subscribers():
                if 'Films🎬' in base.show_subs(s[0]):
                    films_sub.add(s[0])
            NewFilmVK.get_content()
            if NewFilmVK.get_file_date('films.txt') == str(NewFilmVK.date):
                await asyncio.sleep(uniform(1800, 3600))
            else:
                NewFilmVK.write_date('films.txt', NewFilmVK.date)
                for s in films_sub:
                    await bot.send_photo(chat_id=s, photo=NewFilmVK.image,
                                         caption=NewFilmVK.get_content() + 'Смотреть →' + NewFilmVK.url)
        except:
            print('Error')
            await asyncio.sleep(1800)


# Function for Music mailing
# async def get_new_music():
#     while True:
#         music_subs = set()
#         for s in base.show_subscribers():
#             if 'Musics🎵' in base.show_subs(s[0]):
#                 music_subs.add(s[0])
#         id = music.get_id()
#         if music.get_file_id('music.txt') == id:
#             await asyncio.sleep(uniform(300, 500))
#         else:
#             music.write_id('music.txt', id)
#             for s in music_subs:
#                 await bot.send_message(chat_id=s, text=music.get_content())


# Function for Music mailing
async def get_new_music():
    while True:
        music_subs = set()
        for s in base.show_subscribers():
            if 'Musics🎵' in base.show_subs(s[0]):
                music_subs.add(s[0])
        status = mus.get_status()
        if mus.Status == status:
            await asyncio.sleep(uniform(300, 500))
        else:
            mus.Status = status
            for s in music_subs:
                 await bot.send_message(chat_id=s, text='Подписка Musics🎵' + '\n' + 'Новый трек: ' + mus.get_content())