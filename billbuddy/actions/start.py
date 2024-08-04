from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from billbuddy.utils import decorators, cfg, helpers
from billbuddy.resources.dao import user_exists, add_user


@decorators.is_valid_response
async def start_command_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """display message on start command"""
    user = update.message.from_user
    if await user_exists(user.id):
        return  # redirect to menu
    await add_user(first_name=user.first_name, tg_id=user.id, username=user.username)

    msg_template: str = cfg("start.toml").get("START")["en"]
    keyboard_template: list = cfg("start.toml").get("KEYBOARDS")["en"]

    msg = msg_template.format(user.first_name)
    await update.message.reply_text(
        msg,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=ReplyKeyboardMarkup(
            helpers.create_keyboard_button(keyboard_template), resize_keyboard=True
        ),
    )
