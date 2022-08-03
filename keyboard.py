from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

quest = 'Задать вопрос'
order = 'Сделать заказ'
site = 'Сайт'
market = InlineKeyboardButton('Рекламный ролик', callback_data='market_o')
clip = InlineKeyboardButton('Снять видеоклип', callback_data='clip_o')
kf = InlineKeyboardButton('Короткометражный фильм', callback_data='kf_o')

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(quest, order).add(site)
kb_order = InlineKeyboardMarkup().row(market, clip).add(kf)
