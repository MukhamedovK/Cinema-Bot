from aiogram.types import *

async def start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        KeyboardButton("🔍 Поиск"),
        KeyboardButton("🔥 Популярное"),
        KeyboardButton("🗄 Фильмы"),
        KeyboardButton("🗂 Сериалы"),
        KeyboardButton("⭐️ Закладки"),
        KeyboardButton("👨‍💻 Информация"),
    )

    return btn

async def search_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row("⤴️ Вернуться")
    btn.add(
        KeyboardButton("🕵️‍♂️ Что ищут другие"),
        KeyboardButton("⚙️ Фильтр"),
    )

    return btn

async def popularny_inline_btn():
    btn = InlineKeyboardMarkup(resize_keyboard=True, row_width=5)
    btn.add(
        InlineKeyboardButton("1", callback_data="1"),
        InlineKeyboardButton("2", callback_data="2"),
        InlineKeyboardButton("3", callback_data="3"),
        InlineKeyboardButton("4", callback_data="4"),
        InlineKeyboardButton("5", callback_data="5"),
    )

    btn.add(
        InlineKeyboardButton("[ все ]", callback_data="4"),
        InlineKeyboardButton("фильмы", callback_data="5"),
        InlineKeyboardButton("сериалы", callback_data="6"),

    )

    btn.add(
        InlineKeyboardButton("Страница: 1", callback_data="7"),
        InlineKeyboardButton("Вперед ⏭", callback_data="8"),
    )

    return btn

async def popularny_reply_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    btn.add(
        KeyboardButton("⤴️ Вернуться"),
    )

    return btn


async def film_serial_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row("⤴️ Вернуться")
    btn.add(
        KeyboardButton("Недавно добавленные"),
        KeyboardButton("Топ рейтинга"),
        KeyboardButton("Случайный Материал"),
        KeyboardButton("По жанру"),
        KeyboardButton("По году"),
        KeyboardButton("Вы смотрели"),
    )

    return btn

async def zakladki_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row("⤴️ Вернуться")

    return btn

async def information_btn():
    btn = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        InlineKeyboardButton("💎 Купить подписку", url="youtube.com"),
        InlineKeyboardButton("❤️ Что дает PREMIUM", callback_data="10"),
        InlineKeyboardButton("🧐 Ответы на Вопросы", url="youtube.com"),

    )

    return btn