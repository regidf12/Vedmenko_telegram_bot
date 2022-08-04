import os
from datetime import datetime
import random
import re
import json

import telebot

TOKEN = os.environ.get('TOKEN')

rr = """Эксклюзивный видеоролик сделает ваш бренд узнаваемым, привлечет большее количество потенциальных клиентов. Наша команда создаст качественный видео-контент, который будет отличаться на фоне конкурентов.
Стоимость: от 18 500₽"""
sv = """Уникальный и стильный клип, который будет неповторимым и повысит узнаваемость артиста. Наша команда создаст творческий клип по всем трендам индустрии, что не оставит равнодушным зрителя.
Стоимость: от 10 500₽"""
kk = """Создания короткометражного фильма по вашему сценарию или под ключ. Наша команда обладает свежим и прогрессивным мышлением, что позволяет создать умное и важное кино.
Стоимость: от 100 000₽"""
an = "Сделать заказ вы можете, через наш сайт или задать вопрос и наша команда ответит вам и обработает ваш заказ"

quest = '/question'
order = '/price'
site = '/site'

ads = '/ads'
video_clip = '/video_clip'
short_film = '/short_film'

kb_order = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(ads, video_clip).add(short_film)
kb_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(quest, order).add(site)

bot = telebot.TeleBot(token=TOKEN, threaded=False)


def echo(message, username):
    if message.sticker:
        _bot_send_message_with_retry(message.chat.id, message.sticker.file_id,
                                     reply_to_message_id=message.message_id)
    else:
        answer = f'Мне не понятно это сообщение: {message.text}, {username}?'
        _bot_send_message_with_retry(message.chat.id, answer,
                                     reply_to_message_id=message.message_id)


def start(message):
    start_message = """. Vedmenko Production - это молодой, перспективный Видеопродакшн. Наша команда делает творческий и качественный фото-видеоконтент, который популяризирует ваш бренд, привлекает большое количество клиентови дарит много позитивных эмоций от готового продукта. Пропишите /help для получения информации о командах."""
    do_order = "Что вас интересует?"
    _bot_send_message_with_retry(message.chat.id, f'{"Здрасвтуйте, " + str(message.from_user.first_name)}' + start_message)
    bot.send_message(message.chat.id, do_order, reply_markup=kb_menu)


def help(message):
    info = "Список команд и их значение:\n" \
           "/start - начало работы с ботом \n" \
           "/help - описывает информацию о командах\n" \
           "/question - где можно задать вопрос\n" \
           "/price - информация об услугах\n" \
           "/site - ссылка на наш сайт\n" \
           "/ads - Рекламный ролик\n" \
           "/video clip - Видео клип\n" \
           "/short film - Короткометражный фильм"
    bot.send_message(message.chat.id, info, reply_markup=kb_menu)


def quest(message):
    resp = "Задайте свой вопрос здесь: "
    _bot_send_message_with_retry(message.chat.id, resp + 'https://t.me/vedmenkoprod')
    bot.send_message(message.chat.id, "На ваш вопрос ответят в течении 24 часов", reply_markup=kb_menu)                             


def order(message):
    bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=kb_order)


def ads(message):
    _bot_send_message_with_retry(message.chat.id, rr)
    bot.send_message(message.chat.id, an, reply_markup=kb_menu)


def vc(message):
    _bot_send_message_with_retry(message.chat.id, sv)
    bot.send_message(message.chat.id, an, reply_markup=kb_menu)


def sf(message):
    _bot_send_message_with_retry(message.chat.id, kk)
    bot.send_message(message.chat.id, an, reply_markup=kb_menu)


def site(message):
    show_site = "https://vedmenkoprod.ru/"
    bot.send_message(message.chat.id, f'{"Наш сайт: " + show_site}', reply_markup=kb_menu)


def route_command(command, message):
    if command == '/start':
        return start(message)
    if command == '/help':
        return help(message)
    elif command == '/question':
        return quest(message)
    elif command == '/price':
        return order(message)
    if command == '/ads':
        return ads(message)
    if command == '/video_clip':
        return vc(message)
    if command == '/short_film':
        return sf(message)
    elif command == '/site':
        return site(message)
    else:
        bot.send_message(message.chat.id, "Неизвестная команда, простите.", reply_markup=kb_menu)


def _bot_send_message_with_retry(chat_id, text, **kwargs):
    try:
        return bot.send_message(chat_id, text, **kwargs)
    except telebot.apihelper.ApiTelegramException as e:
        if e.error_code == 400:
            if 'reply_to_message_id' in kwargs:
                del kwargs['reply_to_message_id']
            return bot.send_message(chat_id, text, **kwargs)


def main(**kwargs):
    print(f'Received: "{kwargs}"')
    message = telebot.types.Update.de_json(kwargs)
    message = message.message or message.edited_message
    if message and message.text and message.text[0] == '/':
        print(f'Echo on "{message.text}"')
        route_command(message.text.lower(), message)
    else:
        echo(message, message.chat.username)
