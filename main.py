# core.telegram.org/bots/webapps    # website for more info
from aiogram import Bot, Dispatcher, executor, types  # pip install aiogram==2.23
from aiogram.types.web_app_info import WebAppInfo
import logging
import json

logging.basicConfig(level=logging.INFO)
bot = Bot('7249082193:AAFfFknA-8lumYkCs98nlmJrTLe0pFHArno')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Open web page', web_app=WebAppInfo(url='https://66f57f7320784b291e49fafa--boisterous-sunshine-1fd28c.netlify.app')))
    await message.answer('Hello my Friend', reply_markup=markup)


@dp.message_handler(content_types=['web-app-data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}')


if __name__ == '__main__':
    executor.start_polling(dp)
