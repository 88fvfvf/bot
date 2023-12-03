import telebot
from currency_converter import CurrencyConverter
from telebot import types


bot = telebot.TeleBot('5897762142:AAG_-k8DMjxeYAR3VGOB2bu3HpUCCs6Q1uU')
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в бот-калькулятор валют.\nВведите Сумму:')
    bot.register_next_step_handler(message,summa)

def summa(message):
    global amount
    try:    
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id,'Ошибка.Пожалуйста проверьте указанную вами сумму')
        bot.register_next_step_handler(message,summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Другая Валюта', callback_data='else')
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id,'Выберите Пару Валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id,'Ошибка.Число должно быть больше 0')
        bot.register_next_step_handler(message,summa)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0],values[1])
        bot.send_message(call.message.chat.id, f'Получается: {round(res,2)}\nМожете Заново вписать Сумму')
        bot.register_next_step_handler(call.message,summa)
    else:
        bot.send_message(call.message.chat.id,'Введите пару через /\nПример EUR/UZS')
        bot.register_next_step_handler(call.message,mycur)


def mycur(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0],values[1])
        bot.send_message(message.chat.id, f'Получается: {round(res,2)}\nМожете Заново вписать Сумму')
        bot.register_next_step_handler(message,summa)
    except Exception:
        bot.send_message(message.chat.id, 'Вы написали неверно пожалуста введите правильно\nне Забудьте /')
        bot.register_next_step_handler(message,summa)


bot.polling(none_stop=True)
