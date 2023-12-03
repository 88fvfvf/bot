from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json
import config



bot = Bot(config.TOKEN_BOT)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Войти',web_app= WebAppInfo(url = 'https://ninjadeveloperss.github.io/TestX/#')))
    await message.answer('Пожалуйста Войдите в систему',reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message:types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res ["name"]}\nPassword: {res ["password"]}\nPhone: {res["phone"]}\nEmail: {res["email"]}')
    await message.answer("Вы успешно зашли")


    # donate

@dp.message_handler(commands=['donate'])
async def donate(message:types.Message):
    await bot.send_invoice(message.chat.id, 'Общий счёт заказа','Оплата Заказа','HUMO BURGER', config.PAYMENT,'UZS', [types.LabeledPrice('Общий счёт заказа',13000 * 100)])
        

@dp.message_handler(content_types= types.ContentType.SUCCESSFUL_PAYMENT)
async def success(message:types.Message):
    await message.answer(f'платёж успешно выполнен:{message.successful_payment.order_info}')

# donate end

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)