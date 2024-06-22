from aiogram import types
def keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="-", callback_data="option1")
    button2 = types.InlineKeyboardButton(text="1", callback_data="option2")
    keyboard.add(button1, button2)
    button3 = types.InlineKeyboardButton(text="+", callback_data="option3")
    keyboard.add(button3)
    button4 = types.InlineKeyboardButton(text="back", callback_data="option4")
    keyboard.add(button4)