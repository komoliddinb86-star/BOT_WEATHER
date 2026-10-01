from telebot import TeleBot
from telebot.types import Message
from keyboards import *
import requests
TOKEN ="8605258412:AAHnN37YihnMUTAERci1GaBvWhdp9sFIUh4"



bot=TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def command_start(message:Message):
    chat_id=message.chat.id
    bot.send_message(chat_id,'Salom! Men ob-xavo botiman\n'
                             'Ob-xavoni bilish uchun tugmani bosing',
                     reply_markup=generate_button())

@bot.message_handler(regexp='ob-xavo')
def ask_city(message:Message):
    chat_id=message.chat.id
    msg=bot.send_message(chat_id,'Shaxarni nomini kiriting va kuting:')
    bot.register_next_step_handler(msg,answer_to_user)


def answer_to_user(message:Message):
    chat_id=message.chat.id
    text=message.text
    bot.send_message(chat_id,f'Siz kiritgan shaxar: {text}')

    KEY="6418b539e0697f54de8a3df65ebe9444"
    params={
        'appid':KEY,
        'units':'metric',
        'lang':'ru',
        'q':text
    }

    data=requests.get('https://api.openweathermap.org/data/2.5/weather',params=params).json()

    temp=data['main']['temp']
    wind_speed=data['wind']['speed']
    description=data['weather'][0]['description']
    answer=f'{text} {description}\nXarorat: {temp}\n shamol tezligi: {wind_speed}'
    bot.send_message(chat_id,answer)
    ask_again(message)

def ask_again(message:Message):
    chat_id=message.chat.id
    bot.send_message(chat_id,'Yana shaxar nomini kiriting',reply_markup=generate_button())






bot.polling(none_stop=True)