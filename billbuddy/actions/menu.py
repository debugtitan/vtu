from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from billbuddy.resources.dao.users import get_user
from billbuddy.utils import cfg, helpers


async def main_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """main menu for bill point"""
    try:
        user_id = update.message.from_user.id
    except AttributeError as err:
        user_id = update.callback_query.from_user.id
    user = await get_user(user_id) or await get_user(user_id)
    button = cfg("menu.toml").get("KEYBOARDS")[user.language_code]
    msg_template = cfg("menu.toml").get("MESSAGE")[user.language_code]
    await context.bot.send_message(
        user.tg_id,
        msg_template,
        reply_markup=ReplyKeyboardMarkup(
            helpers.create_keyboard_button(
                buttons=button["buttons"],
                buttons_per_column=3,
                button_header=button["headers"],
                button_footer=button["footers"],
            ),
            resize_keyboard=True,
            one_time_keyboard=True,
        ),
    )
