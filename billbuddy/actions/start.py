from telegram import Update
from telegram.ext import ContextTypes

from billbuddy.utils import decorators

@decorators.threaded
@decorators.is_valid_response
async def  start_command_handler(update: Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    """ display message on start command """
    print(update)