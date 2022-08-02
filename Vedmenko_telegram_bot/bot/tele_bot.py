import telebot

from config import TOKEN
from messages import MESSAGES
from keyboard import kb_menu, kb_order

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.send_message(message.from_user.id, f'{"Здрасвтуйте, " + str(message.from_user.first_name)}' + MESSAGES['start'],
                     reply_markup=kb_menu)


@bot.message_handler()
def quest(message):
    if message.text == 'Задать вопрос':
        bot.send_message(message.from_user.id, "Задайте свой вопрос тут: " + "https://t.me/vedmenkoprod")
        bot.send_message(message.from_user.id, "На ваш впорос ответят в течении 24 часов")
    if message.text == 'Сайт':
        bot.send_message(message.from_user.id, "Наш сайт: " + "https://vedmenkoprod.ru/")
    if message.text == 'Сделать заказ':
        bot.send_message(message.from_user.id, "Что вас интересует?", reply_markup=kb_order)
    if message.text == "Рекламный ролик":
        bot.send_message(message.from_user.id, MESSAGES['rr'])
        bot.send_message(message.from_user.id, MESSAGES['an'], reply_markup=kb_menu)
    if message.text == "Снять видеоклип":
        bot.send_message(message.from_user.id, MESSAGES['sv'])
        bot.send_message(message.from_user.id, MESSAGES['an'], reply_markup=kb_menu)
    if message.text == "Короткометражный фильм":
        bot.send_message(message.from_user.id, MESSAGES['kk'])
        bot.send_message(message.from_user.id, MESSAGES['an'], reply_markup=kb_menu)


bot.polling(none_stop=True, interval=0)
