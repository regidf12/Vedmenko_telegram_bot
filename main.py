import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from messages import MESSAGES

TOKEN = ''
SBTOKEN = ''

quest = 'Задать вопрос'
order = 'Сделать заказ'
site = 'Сайт'
buy = 'Поддержать разработчика'
error = 'Сообщить об ошибке'
market = InlineKeyboardButton('Рекламный ролик', callback_data='market_o')
clip = InlineKeyboardButton('Снять видеоклип', callback_data='clip_o')
kf = InlineKeyboardButton('Короткометражный фильм', callback_data='kf_o')
site_blur_but = InlineKeyboardButton('Vedmenko poduction', url="https://vedmenkoprod.ru/")
quest_blur_but = InlineKeyboardButton('Vedmenko poduction', url="https://t.me/vedmenkoprod")
error_blur_but = InlineKeyboardButton('Сообщить об ошибке', url="https://t.me/white_prince_0")


kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(quest, order).add(site).add(buy).\
    add(error)
kb_order = InlineKeyboardMarkup().row(market, clip).add(kf)
kb_site = InlineKeyboardMarkup().add(site_blur_but)
kb_quest = InlineKeyboardMarkup().add(quest_blur_but)
kb_error = InlineKeyboardMarkup().add(error_blur_but)

logging.basicConfig(level=logging.INFO)
loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot, loop=loop)
PRICE = types.LabeledPrice(label='Поддержать разработчика', amount=10000)


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


@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(commands=['start', 'help'])
async def start_cmd(message: types.Message):
    await bot.send_message(message.chat.id,
                           f'{"Здрасвтуйте, " + str(message.from_user.first_name)}' + MESSAGES['start'],
                           reply_markup=kb_menu)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    print('successful_payment:')
    pmnt = message.successful_payment.to_python()
    for key, val in pmnt.items():
        print(f'{key} = {val}')

    await bot.send_message(message.chat.id, MESSAGES['successful_payment'].format(
        total_amount=message.successful_payment.total_amount // 100,
        currency=message.successful_payment.currency
    )
                           )
    await bot.send_message(message.chat.id, MESSAGES['term'])


@dp.message_handler()
async def menu(message: types.Message):
    if message.text == 'Задать вопрос':
        await bot.send_message(message.chat.id, "Задайте свой вопрос тут", reply_markup=kb_quest)
        await bot.send_message(message.chat.id, "Вам ответят максимально быстро")
    elif message.text == 'Сделать заказ':
        await bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=kb_order)
    elif message.text == 'Сайт':
        await bot.send_message(message.chat.id, "На нашем сайте, вы можете оформить заказ, задать вопрос или получить "
                                                "больше информации о нас.", reply_markup=kb_site)
    elif message.text == 'Поддержать разработчика':
        await bot.send_message(message.chat.id, "В данный момент оплата Юкасса не поддерживает оплату telegram")
    elif message.text == 'Сообщить об ошибке':
        await bot.send_message(message.chat.id, "Заметили ошибку? Cообщите о ней разработчику <3",
                               reply_markup=kb_error)
    else:
        answer = f'Мне не понятно это сообщение: {message.text}, {message.from_user.first_name}?'
        await bot.send_message(message.chat.id, answer)


@dp.message_handler()
async def process_buy_command(message: types.Message):
    await bot.send_invoice(
        message.chat.id,
        title='Поддержите разработчика',
        description='Я тоже хочу кушать',
        provider_token=SBTOKEN,
        currency='rub',
        photo_url='https://i.pinimg.com/736x/8b/08/92/8b08924c7e10c38d4a9c487a15c428d3.jpg',
        photo_height=512,
        photo_width=512,
        photo_size=512,
        is_flexible=False,
        prices=[PRICE],
        start_parameter='support_developer',
        payload='some-invoice-payload-for-our-internal-use'
    )


@dp.message_handler(content_types=ContentType.ANY)
async def echo_stiker(message: types.Message):
    if message.sticker:
        await bot.send_sticker(message.chat.id,
                               "CAACAgIAAxkBAAIEIWLsLV0pWA_sL8ZHpsPE6JIQQnM-AAK8GQACnX5gSypUlj4bLhX1KQQ")


if __name__ == '__main__':
    executor.start_polling(dp, loop=loop)
