"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""


import logging

from os import environ

import ephem
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


async def planet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return
    user_text: str = context.args[0].strip().capitalize()
    logging.info(user_text)
    try:
        planet_class = getattr(ephem, user_text)
        user_planet = planet_class()

        user_planet.compute()

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Планета {user_text} "
            f"сейчас находится в созвездии {ephem.constellation(user_planet)[1]}",
        )
        return

    except AttributeError:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Не правильно введено имя планеты"
        )
        return


if __name__ == "__main__":
    application = ApplicationBuilder().token(environ["TOKEN"]).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    planet_handler = CommandHandler("planet", planet)
    application.add_handler(planet_handler)

    application.run_polling()
