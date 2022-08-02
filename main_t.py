import asyncio

from telebot.async_telebot import AsyncTeleBot
from config_t import TOKEN
from messages_t import MESSAGES
from keyboard_t import kb_menu, kb_order

bot = AsyncTeleBot(TOKEN)


@bot.message_handler(commands=['start'])
async def start_cmd(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, f'{"Здрасвтуйте, " + str(message.from_user.first_name)}' + MESSAGES['start'],
                           reply_markup=kb_menu)


@bot.message_handler()
async def quest(message):
    chat_id = message.from_user.id
    if message.text == 'Задать вопрос':
        await bot.send_message(chat_id, "Задайте свой вопрос тут: " + "https://t.me/vedmenkoprod")
        await bot.send_message(chat_id, "На ваш впорос ответят в течении 24 часов")
    if message.text == 'Сайт':
        await bot.send_message(chat_id, "Наш сайт: " + "https://vedmenkoprod.ru/")
    if message.text == 'Сделать заказ':
        await bot.send_message(chat_id, "Что вас интересует?", reply_markup=kb_order)
    if message.text == "Рекламный ролик":
        await bot.send_message(chat_id, MESSAGES['rr'])
        await bot.send_message(chat_id, MESSAGES['an'], reply_markup=kb_menu)
    if message.text == "Снять видеоклип":
        await bot.send_message(chat_id, MESSAGES['sv'])
        await bot.send_message(chat_id, MESSAGES['an'], reply_markup=kb_menu)
    if message.text == "Короткометражный фильм":
        await bot.send_message(chat_id, MESSAGES['kk'])
        await bot.send_message(chat_id, MESSAGES['an'], reply_markup=kb_menu)

asyncio.run(bot.polling())
