from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton('NEXT', callback_data='quiz_2_button')
    markup.add(button_2)
    question = "Президент Росии?"
    answer = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]


    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Иди учись",
        open_period=10,
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):
    question = "Сколько??"
    answer = [
        '4',
        '8',
        '4, 6',
        '2, 4',
        '5',
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Стыдно не знать",
        open_period=5,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='quiz_1_button')
    dp.register_callback_query_handler(quiz_3, text='quiz_2_button')
