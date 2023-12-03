from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5960630563:AAH7va9KPMdjgIUinFnMKOIyurpMtACB8Jk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    # await bot.send_message(message.chat.id , 'hello Users')
    # await message.answer('answer')
    await message.reply('hello i am perly text')

@dp.message_handler(text='Начать')
async def info(message:types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('site', url='https://google.com'))
    markup.add(types.InlineKeyboardButton('hello',callback_data='hello i am Bot'))
    await message.reply('this is button', reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)



@dp.message_handler(text='none')
async def reply(message:types.Message):
    buttonreply = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    buttonreply.add(types.KeyboardButton('Reply button-1'))
    buttonreply.add(types.KeyboardButton('Reply button-2'))
    await message.answer('this is ReplyButton',reply_markup=buttonreply)


@dp.message_handler() 
async def two(message:types.Message):
    if message.text == 'Reply button-1':
        await message.answer('this is If')
    elif message.text == 'Reply button-2':
        await message.answer('this is If')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)