from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from billbuddy.resources.dao.users import get_user
from billbuddy.utils import cfg, helpers, decorators


@decorators.is_valid_response
async def main_menu_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
):
    """main menu for bill point"""
    user_lang = kwargs.get("lang", "en")
    button = cfg("menu.toml").get("KEYBOARDS")[user_lang]
    msg_template = cfg("menu.toml").get("MESSAGE")[user_lang]
    await context.bot.send_message(
        kwargs.get("id"),
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
