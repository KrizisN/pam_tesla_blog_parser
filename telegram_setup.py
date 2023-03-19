import telegram
from telegram.ext import Updater, CommandHandler

from config import config


def send_message(title, link):
    bot = telegram.Bot(token=config.BOT_TOKEN)
    message = f'New article: {title}\nLink: {"https://www.tesmanian.com/" + link}'
    bot.send_message(chat_id=config.CHAT_ID, text=message)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Welcome to the Tesmanian scraper!"
    )


def run_telegram_bot():
    updater = Updater(config.BOT_TOKEN, use_context=True)

    start_handler = CommandHandler("start", start)
    updater.dispatcher.add_handler(start_handler)

    updater.start_polling()
