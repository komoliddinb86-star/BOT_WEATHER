from telebot.types import ReplyKeyboardMarkup,KeyboardButton


def generate_button():
    markup=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    btn=KeyboardButton(text='Ob-xavo')
    markup.add(btn)
    return markup

