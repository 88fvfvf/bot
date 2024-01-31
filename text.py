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

telegram_key = '6683253948:AAGkgcEwFb4pYfPnZeziAM6KOzSjm45ctp0'
openai.api_key = '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'

bot = telebot.TeleBot(telegram_key)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Salom! Men - sun'iy intellektman, men misollar va masalarar yechimini topishda Test yechishda  ishlatishingiz mumkun!\n\n🤖 Men kimlar uchun mo'ljallanganman: maktabda yoki institutda o'qidiganlar uchun, chunki har qanday masalada yordam bera olaman.")


@bot.message_handler(content_types=['text'])
def main(message):
    img = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(img)
    reply = ''
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message.text,
        max_tokens=1000,
        temperature=0.9,
        n=10,
        stop=None
    )   
    if response and response.choices:
        reply = response.choices[0].text.strip()
        txt = textwrap.wrap(reply, width=70)

        y = 100  # Initial y-coordinate
        for line in txt:
            draw.text((70, y), line, font=font, fill=(0, 0, 0))
            y += 30  # Increase the y-coordinate for the next line

        img.save('image.jpg')
        bot.send_photo(message.chat.id, photo=open('image.jpg', 'rb'))
        os.remove('image.jpg')
    else:
        reply = 'Oops... something went wrong.'

    bot.send_message(message.chat.id, reply)


bot.polling(none_stop=True)
