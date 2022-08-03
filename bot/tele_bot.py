import telebot

from config import TOKEN
from telebot.types import ReplyKeyboardMarkup

bot = telebot.TeleBot(TOKEN)

start_message = """. Vedmenko Production - это молодой, перспективный Видеопродакшн. Наша команда делает творческий и качественный фото-видеоконтент, который популяризирует ваш бренд, привлекает большое количество клиентови дарит много позитивных эмоций от готового продукта."""
do_order = "Что вас интересует?"
do_quest = "Задайте свой вопрос"
do_site = "https://vedmenkoprod.ru/"
answer = ". Вам пришло сообщение"
rr = """Эксклюзивный видеоролик сделает ваш бренд узнаваемым, привлечет большее количество потенциальных клиентов. Наша команда создаст качественный видео-контент, который будет отличаться на фоне конкурентов.
Стоимость: от 18 500₽"""
sv = """Уникальный и стильный клип, который будет неповторимым и повысит узнаваемость артиста. Наша команда создаст творческий клип по всем трендам индустрии, что не оставит равнодушным зрителя.
Стоимость: от 10 500₽"""
kk = """Создания короткометражного фильма по вашему сценарию или под ключ. Наша команда обладает свежим и прогрессивным мышлением, что позволяет создать умное и важное кино.
Стоимость: от 100 000₽"""
an = "Сделать заказ вы можете, через наш сайт или задать вопрос и наша команда ответит вам и обработает ваш заказ"
quest = 'Задать вопрос'
order = 'Сделать заказ'
site = 'Сайт'
market = 'Рекламный ролик'
clip = 'Снять видеоклип'
kf = 'Короткометражный фильм'

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(quest, order).add(site)
kb_order = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(market, clip).add(kf)
MESSAGES = {
    'start': start_message,
    'order': do_order,
    'quest': do_quest,
    'site': do_site,
    'answer': answer,
    'rr': rr,
    'sv': sv,
    'kk': kk,
    'an': an,
}


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
