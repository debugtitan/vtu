from telegram import Update
from telegram.ext import ContextTypes

from billbuddy.utils import constants, decorators, cfg


@decorators.is_valid_response
async def start_command_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """display message on start command"""
    user = update.message.from_user
    user_id = user.id
    username = user.username
    first_name = user.first_name
    language_code = user.language_code
    is_premium_account = user.is_premium
    msg_temp: str = cfg.get("START").get(language_code, cfg.get("START").get("en"))
    msg = msg_temp.format(first_name.capitalize())

    await update.message.reply_text(msg, reply_markup=constants.start_menu())
