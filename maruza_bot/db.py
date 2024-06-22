import wikipedia
import aiogram
import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN='7272422006:AAG7PgJoLuKBgqCXmRdatM90FRE3oYSQS5E'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    await message.reply(f"{first_name} siz menga istalgan mavzu ayting men szga inglizchada malumot beraman")

@dp.message_handler()
async def maruza(meseege: types.Message):
    try:
        respond=wikipedia.summary(meseege.text)
        await meseege.answer(respond)
    except:
        await meseege.answer("bu mavzuga oid maulot bilmeman")
if __name__ == '__main__':
     executor.start_polling(dp, skip_updates=True)
"""hali keyingi darslarga bu botni rivojlantirib koproq malumot qushaman
wikipidea kutubxonasini urganib quldan keguncha yaratishga harakat qildm"""

