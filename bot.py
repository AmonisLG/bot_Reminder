import time
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)


TOKEN = "6107422905:AAFyI9n2k_KQ2LfdiX2iP62Pku8mt_KWVIc"
MSG = "Нужно оплатить штраф за нарушение ПДД до 10.04.2023!!!!"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Привет,{user_full_name}!")
    for i in range(4):
        time.sleep(3*24)
        await bot.send_message(user_id, MSG.format(user_name))

if  __name__=='__main__':
    executor.start_polling(dp)




