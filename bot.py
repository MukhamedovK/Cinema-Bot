import logging

from aiogram import Dispatcher, Bot, executor
from aiogram.types import *
from btn import start_btn, search_btn, popularny_reply_btn, popularny_inline_btn, film_serial_btn, zakladki_btn, information_btn


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "6251779786:AAG3lZJXf7u2-r7rBOW29ZhSiCbEL7ZF3zw"

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    btn = await start_btn()
    await message.answer(f"Приветствую тебя в нашем кинотеатре!\n\n"
                        "Популярные фильмы, новинки, сериалы ищите здесь 😉\n\n"
                        "🌀 Зеркало бота: @ActualMirrorBot\n\n"
                        "🤟 Приятного использования!\n\n", reply_markup=btn)
    
@dp.message_handler()
async def text_bot(message: Message):
    text = message.text
    if text == "🔍 Поиск":
        btn = await search_btn()
        await message.answer("🔍 Какой фильм или сериал будем искать?\n"
                            "Ищем: <i>по названию</i>", reply_markup=btn)

    elif text == "🔥 Популярное":
        btn = await popularny_reply_btn()
        btn2 = await popularny_inline_btn()
        await message.answer("🔥 Популярное", reply_markup=btn)
        await message.answer("1) Тайлер Рейк: Операция по спасению 2 (2023)\n"
                            "<code>КП: 0.00 | IMDb: 8.10 | боевик | 02:02</code>\n"
                            "2) Флэш (2023)\n"
                            "<code>КП: 6.50 | IMDb: 7.80 | боевик | 02:24</code>\n"
                            "3) Волк с Уолл-стрит (2013)\n"
                            "<code>КП: 7.90 | IMDb: 8.20 | биография | 03:00</code>\n"
                            "4) Человек-паук: Через вселенные 2 (2022)\n"
                            "<code>КП: 0.00 | IMDb: 0.00 | боевик | 00:00</code>\n"
                            "5) Джордж Форман: Несокрушимый (2023)"
                            "<code>КП: 0.00 | IMDb: 6.60 | биография | 02:09</code>\n", reply_markup=btn2)

    elif text == "🗄 Фильмы":
        btn = await film_serial_btn()
        await message.answer("Выберите раздел", reply_markup=btn)

    elif text == "🗂 Сериалы":
        btn = await film_serial_btn()
        await message.answer("Выберите раздел", reply_markup=btn)

    elif text == "⭐️ Закладки":
        btn = await zakladki_btn()
        await message.answer("⭐️ Закладки", reply_markup=btn)

    elif text == "👨‍💻 Информация":
        btn = await information_btn()
        await message.answer("💻 Зеркало бота: @ActualMirrorBot\n\n"
                            "💎 Продлить/купить подписку: @EasyPayRo_bot\n\n"
                            "Твой PREMIUM: отсутствует ☹️\n\n", reply_markup=btn)

    elif text == "⤴️ Вернуться":
        btn = await start_btn()
        await message.answer("Вы находитесь в главном меню", reply_markup=btn)



if __name__ == '__main__':
    executor.start_polling(dp)