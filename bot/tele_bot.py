import logging

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from messages import MESSAGES
from keyboard import kb_menu, kb_order

logging.basicConfig(level=logging.INFO)
m_id = '300226190'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.callback_query_handler(lambda c: c.data == 'market_o')
async def cb_market(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES['rr'])
    await bot.send_message(callback_query.from_user.id, MESSAGES['an'])


@dp.callback_query_handler(lambda c: c.data == 'clip_o')
async def callback_clip(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES['sv'])
    await bot.send_message(callback_query.from_user.id, MESSAGES['an'])


@dp.callback_query_handler(lambda c: c.data == 'kf_o')
async def callback_kf(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES['kk'])
    await bot.send_message(callback_query.from_user.id, MESSAGES['an'])


@dp.message_handler(commands=['start', 'help'])
async def start_cmd(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{"Здрасвтуйте, " + str(message.from_user.first_name)}' + MESSAGES['start'],
                           reply_markup=kb_menu)


@dp.message_handler()
async def menu(message: types.Message):
    if message.text == 'Задать вопрос':
        await bot.send_message(message.from_user.id, "Задайте свой вопрос тут: " + "https://t.me/vedmenkoprod")
        await bot.send_message(message.from_user.id, "На ваш впорос ответят в течении 24 часов")
    elif message.text == 'Сделать заказ':
        await bot.send_message(message.from_user.id, "Что вас интересует?", reply_markup=kb_order)
    elif message.text == 'Сайт':
        await bot.send_message(message.from_user.id, "Наш сайт: " + 'https://vedmenkoprod.ru/')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
