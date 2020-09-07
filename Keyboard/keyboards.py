from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Keyboard.Callback import subscribe_callback

# Keyboard for subscribe
subscriptions = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='News📝',
                                 callback_data=subscribe_callback.new(website='News📝', status='True')),
            InlineKeyboardButton(text='Habr-IT blog💻', callback_data='subscribe:Habr-IT blog💻:True'),
            InlineKeyboardButton(text='Games🎮', callback_data='subscribe:Games🎮:True'),
            InlineKeyboardButton(text='Films🎬', callback_data='subscribe:Films🎬:True'),
            InlineKeyboardButton(text='Musics🎵', callback_data='subscribe:Musics🎵:True')
        ],
        [InlineKeyboardButton(text='Отмена❌', callback_data='cancel')]
    ]
)

# Keyboard for unsubscribe
unsubscriptions = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='News📝',
                                 callback_data=subscribe_callback.new(website='News📝', status='False')),
            InlineKeyboardButton(text='Habr-IT blog💻', callback_data='subscribe:Habr-IT blog:False💻‍'),
            InlineKeyboardButton(text='Games🎮', callback_data='subscribe:Games🎮:False'),
            InlineKeyboardButton(text='Films🎬', callback_data='subscribe:Films🎬:False'),
            InlineKeyboardButton(text='Musics🎵', callback_data='subscribe:Musics🎵:False')
        ],
        [InlineKeyboardButton(text='Отмена❌', callback_data='cancel')]
    ]
)