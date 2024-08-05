from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from billbuddy.utils import decorators


@decorators.is_valid_response
async def help_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
):
    """"""
