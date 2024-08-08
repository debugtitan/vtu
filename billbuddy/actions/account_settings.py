from telegram import Update
from telegram.ext import ContextTypes

from billbuddy.utils import decorators

@decorators.is_valid_response
async def account_settings_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
    """ """