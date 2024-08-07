from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from billbuddy.actions.menu import main_menu_handler
from billbuddy.utils import decorators, cfg, helpers
from billbuddy.resources.dao import user_exists, add_user


@decorators.is_valid_response
async def start_command_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
) -> None:
    """display message on start command"""
    user = update.message.from_user
    if await user_exists(user.id):
        keyboard_template: list = cfg("start.toml").get("KEYBOARDS")["en"]
        return await main_menu_handler(update, context)
    await add_user(first_name=user.first_name, tg_id=user.id, username=user.username)

    msg_template: str = cfg("start.toml").get("START")["en"]
    keyboard_template: list = cfg("start.toml").get("KEYBOARDS")["en"]

    msg = msg_template.format(user.first_name)
    await update.message.reply_text(
        msg,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
            helpers.create_inline_button(
                buttons=keyboard_template, callback_text="localization#"
            )
        ),
    )
