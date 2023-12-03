import telebot
import requests    
import json 


bot = telebot.TeleBot('6019982474:AAHtGDA-1RH-sKK5df4oykoXNAkJpRVp0fM')
API = 'fd275c43073aa0fdb4b3e14bfc996e16'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет напиши мне о Городе я отправлю погоду о городе!')


@bot.message_handler(content_types=['text'])
def get_weather(message):   
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        markup = telebot.types.InlineKeyboardMarkup()
        temp = data["main"]["temp"]
        markup.add(telebot.types.InlineKeyboardButton(text = f'Узнать больше о погоде {city}',url= f"https://qna.habr.com/q/751035"))
        bot.reply_to(message, f'Сейчас Погода в {city} : {temp}°C',reply_markup=markup)
       



        if temp > 5.0:
    # отправляем эмодзи
            bot.send_message(message.chat.id, text='☀️')
        else:
    # отправляем текст
            bot.send_message(message.chat.id, text='⛅')
    else:
        bot.reply_to(message,'Город не найден пожалуйста напишите правильно')


bot.polling(none_stop=True)