from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from billbuddy.utils import cfg, helpers, enums, decorators


@decorators.is_valid_response
async def localization_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
):
    lang = kwargs.get("lang", "en")
    keyboard_template: list = cfg("start.toml").get("KEYBOARDS")[lang]
    msg = cfg("start.toml").get("LANGUAGE_MESSAGE")[lang]
    await update.message.reply_text(
        msg,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
            helpers.create_inline_button(
                buttons=keyboard_template, callback_text="localization#"
            )
        ),
    )
