from telegram.ext import ContextTypes
from telegram import Update

from billbuddy.utils import decorators

@decorators.is_valid_response
async def language_selection_handler(
    update: Update, callback: ContextTypes.DEFAULT_TYPE, *args, **kwargs
):
    """handle any type of language selected"""
    print(update.message.text)
