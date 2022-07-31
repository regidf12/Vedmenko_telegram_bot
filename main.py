import asyncio

from telebot.async_telebot import AsyncTeleBot
from config import TOKEN, admin_id
from messages import MESSAGES
from keyboard import kb_menu, kb_quest

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
        await bot.send_message(chat_id, "Задайте свой вопрос")
    if message.text == message.text:
        await bot.send_message(chat_id, "Сообщение доставлено, свами свяжутся в этом чате: ")
        await bot.send_message(admin_id, admin_id, f'{"Здрасвтуйте, " + str(message.from_user.first_name)}' + MESSAGES['answer'], reply_to_message_id=message)
        await bot.send_message(chat_id, "Что вас интереусует", reply_markup=kb_menu)


asyncio.run(bot.polling())
