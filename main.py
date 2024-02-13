import json

import openai
import asyncio
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
import time
import math
import os

with open("./config.json", 'r') as jsf:
    json_data = json.load(jsf)
    token = json_data["TOKEN"]
    openai.api_key = json_data["API_KEY"]

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send(message: types.Message):
    await message.answer(
        ' Привет, это бот, реализующий нейросеть ChatGPT в телеграме.\n\n Данный бот может:\n –Ответить на интересующий тебя вопрос.\n –Укоротить твой текст до нескольких предложений.\n –В целом его возможности безграничны, поэтому можешь попробовать что-то еще:)\n\n Для того чтобы начать работу, объясни нейросети что она должна сделать. Например: "О чем этот текст? ..."')


@dp.message_handler()
async def send(message: types.Message):
    await message.answer('Обработка результата запроса📚')
    start = time.time()
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': message.text}
        ],
        temperature=0
    )
    await message.answer(response['choices'][0]['message']['content'])
    end = time.time()
    await message.answer(f"Время обработки запроса: {math.trunc(end - start)} секунд 🕰")
    print(message.text, '\n', len(message.text))


executor.start_polling(dp, skip_updates=True)
