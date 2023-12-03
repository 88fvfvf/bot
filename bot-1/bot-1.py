import telebot
import webbrowser


bot =telebot.TeleBot('6116987549:AAF2Je7k3KKY6lfcPSjcisSOD4DjujfzacQ') #TOKEN BOTA

@bot.message_handler(commands=['site','web'])
def site(message):
    webbrowser.open('https://duck.show/wp-content/uploads/2018/12/fileMini2018-12-12T14-37-11.jpg')



@bot.message_handler(commands=['text'])   #Здесь можно через запятую задавать несколько команд
def main(message):
    bot.send_message(message.chat.id,'<b><em>Постарайтесь получить то, что любите, иначе придется полюбить то, что получили.</em></b>',parse_mode='html')#{message.from_user.first_name} Фамилия Пользователя




@bot.message_handler(commands=['start'])   #Здесь можно через запятую задавать несколько команд
def main(message):
    bot.send_message(message.chat.id, f'hello,{message.from_user.first_name}')#{message.from_user.first_name} Фамилия Пользователя



@bot.message_handler(commands=['help']) 
def main(message):
    bot.send_message(message.chat.id,'<b><em>Вам,нужно помощь?</em></b>', parse_mode='html')#HELP COMMAND


    #Обычную проверку текста лучше писать снизу,что-бы не-было ошибок

@bot.message_handler()
def info(message):
    if message.text.lower() == "hi":
        bot.send_message(message.chat.id, f'hello,{message.from_user.first_name}')#{message.from_user.first_name} Фамилия Пользователя
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID:{message.from_user.id}')







# polling bota

bot.polling(none_stop=True)