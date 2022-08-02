from telebot.types import ReplyKeyboardMarkup

quest = 'Задать вопрос'
order = 'Сделать заказ'
site = 'Сайт'
market = 'Рекламный ролик'
clip = 'Снять видеоклип'
kf = 'Короткометражный фильм'


kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(quest, order).add(site)
kb_order = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(market, clip).add(kf)
