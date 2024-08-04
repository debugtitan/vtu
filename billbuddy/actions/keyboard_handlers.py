from telegram.ext import ContextTypes
from telegram import Update


async def language_selection_handler(
    update: Update, callback: ContextTypes.DEFAULT_TYPE
):
    """handle any type of language selected"""
    print(update.message.text)
