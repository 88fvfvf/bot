import telebot
import sqlite3

bot = telebot.TeleBot('6116987549:AAF2Je7k3KKY6lfcPSjcisSOD4DjujfzacQ')
name = None



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет этот бот создан для сохранение имя и пароль в базе данных')
    conn = sqlite3.connect('Humoyun.ht')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key,name varchar(50),pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id,'Я щас добавлю тебя к базе данных\nваше имя:')
    bot.register_next_step_handler(message,user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id,'Ваш пароль:')
    bot.register_next_step_handler(message,user_pass)

def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('Humoyun.ht')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name,pass) VALUES ('%s','%s')" %(name,password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список Пользователей',callback_data='users'))
    bot.send_message(message.chat.id,'Пользователей Зарегистрирован!', reply_markup=markup)



@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    conn = sqlite3.connect('Humoyun.ht')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info =''
    for el in users:
        info += f'Имя: {el[1]}\nПароль:{el[2]}\n\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id,info)



bot.polling(none_stop=True)