import telebot
from telebot import types
import openai
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

width = 1000
height = 1000
color = (255, 255, 255)  # (R, G, B)
font_size = 24
font = ImageFont.truetype("Roboto-Light.ttf", font_size)

telegram_key = "6683253948:AAGkgcEwFb4pYfPnZeziAM6KOzSjm45ctp0"
openai.api_key = "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"

bot = telebot.TeleBot(telegram_key)

def main(message):
    img = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(img)
    reply = ""  
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.text},
        ],
        max_tokens=500,
        temperature=0.9,
        n=1,
        stop=None,
    )
    if response and response.choices: 
        reply = response.choices[0].message.content.strip()
        txt = textwrap.wrap(reply, width=70)

        y = 100  # Initial y-coordinate
        for line in txt:
            draw.text((70, y), line, font=font, fill=(0, 0, 0))
            y += 30  # Increase the y-coordinate for the next line

        # Check if the message to delete exists
        # if message.message_id - 1 > 0:
        #     try:
        #         bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        #     except telebot.apihelper.ApiTelegramException as e:
        #         print(f"Error deleting message: {e}")

        img.save("image.jpg")
        bot.send_photo(message.chat.id, photo=open("image.jpg", "rb"))
        try:
            os.remove("image.jpg")
        except PermissionError:
            print("PermissionError")
    else:
        reply = "Oops... something went wrong."

    bot.send_message(message.chat.id, reply)
    

def start_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(text="Kanalga obuna bulish",url="https://t.me/usmonuss")
    markup.add(button)
    return markup


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    channel_id = "-1001775723913"

    # Check if the user is a member of the channel
    chat_member = bot.get_chat_member(chat_id=channel_id, user_id=user_id)
    is_subscribed = chat_member.status in [
        "administrator",
        "creator",
        "member",
    ]

    if is_subscribed:
        bot.send_message(message.chat.id,"👋 Salom! Men - sun'iy intellektman, men misollar va masalarar yechimini topishda Test yechishda ishlatishingiz mumkun!\n\n🤖 Men kimlar uchun mo'ljallanganman: maktabda yoki institutda o'qidiganlar uchun, chunki har qanday masalada yordam bera olaman.",)

    else:
        bot.send_message(chat_id, "Botdan foydalanish uchun kanalimizga obuna bo'ling 👇🏻 va qaytatdan yozing",reply_markup=start_markup())

@bot.message_handler(content_types=['text'])
def text(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    channel_id = "-1001775723913"
    try:
        os.remove("image.jpg")
    except FileNotFoundError:
        print("File Not Found")
    # Check if the user is a member of the channel
    chat_member = bot.get_chat_member(chat_id=channel_id, user_id=user_id)
    is_subscribed = chat_member.status in [
        "administrator",
        "creator",
        "member",
    ]

    if is_subscribed:
        bot.send_message(chat_id, "🧠 Hozir o'ylayapman!!\n\nIkki daqiqa ichida javob berolmasam, manga boshidan savol bering!")
        main(message)
    else:
        bot.send_message(chat_id, "Botdan foydalanish uchun kanalimizga obuna bo'ling 👇🏻va qaytatdan yozing",reply_markup=start_markup())


bot.polling(none_stop=True)