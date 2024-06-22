import aiogram
import logging
from aiogram import Bot, Dispatcher, executor, types
from button import keyboard
import asyncio
from app import menu_keybord,menu_data


API_TOKEN="6662673041:AAFDTrFie68ZTzU9c2Z_2AOJaTumNql_R7M"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
db=Dispatcher(bot)

@db.message_handler(lambda message: message.text == "Menyu")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Menyulardan birini tanglang:", reply_markup=menu_keybord)

@db.message_handler(lambda messaage:messaage.text == "menyu1")
async def welcome(message: types.Message):
    await message.answer("xish kelibsz 1-bulimga",reply_markup=menu_data)

@db.message_handler(lambda messaage:messaage.text == "menyu2")
async def welcome(message: types.Message):
    await message.answer("xish kelibsz 2-bulimga",reply_markup=menu_data)
@db.message_handler(lambda messaage:messaage.text == "menyu3")
async def welcome(message: types.Message):
    await message.answer("xish kelibsz 3-bulimga",reply_markup=menu_data)

@db.message_handler(lambda messaage: messaage.text == "menyu4")
async def welcome(message: types.Message):
    await message.answer("xish kelibsz 4-bulimga", reply_markup=menu_data)
@db.message_handler(lambda messaage:messaage.text == "menyu5")
async def welcome(message: types.Message):
    await message.answer("xish kelibsz 5-bulimga",reply_markup=menu_data)
@db.message_handler(lambda messaage:messaage.text == "menyu6")
async def welcome(message: types.Message):
    await message.answer("xish kelibsz 6-bulimga",reply_markup=menu_data)
@db.message_handler(lambda messaage:messaage.text == "menyu7")
async def welcome(message: types.Message):
    await message.answer("xish kelibsz 7-bulimga",reply_markup=menu_data)
@db.message_handler(lambda messaage:messaage.text == "menyu8")
async def welcome(message: types.Message):
    await message.answer("xish kelibsz 8-bulimga",reply_markup=menu_data)
@db.message_handler(lambda messaage:messaage.text == "back")
async def welcome(message: types.Message):
    await message.answer("menyulardan birini tanlang")

@db.message_handler(lambda message: message.text == "Back")
async def show_menu(message: types.Message):
    await message.answer("Back", reply_markup=menu_keybord)
@db.message_handler(lambda message: message.text not in ["Menu"])
async def handle_other_messages(message: types.Message):
    await message.answer("Noto'g'ri so'rov yubordingiz", reply_markup=menu_keybord)
if __name__ == '__main__':
     executor.start_polling(db, skip_updates=True)

