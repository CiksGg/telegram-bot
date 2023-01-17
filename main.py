import requests
from bs4 import BeautifulSoup as BS
from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher.filters import Text

import telebot
from decouple import config
import json


token = config('TOKEN')

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    start_button = ['Все новости']
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(*start_button)


    await message.answer('Лента новостей',reply_markup=keyboard)


@dp.message_handler(commands='quit')
async def start(message:types.Message):
    start_button = []
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(*start_button)
    await message.answer('До свидания',reply_markup=keyboard)


@dp.message_handler(Text(equals='Все новости'))
async def get_news(message:types.Message):
    with open('a.json') as file:
        news_dict = json.load(file)
    for k,v in news_dict.items():
        news = f"{v['title']}\n{v['description']}"

        await message.answer(news)

executor.start_polling(dp)







