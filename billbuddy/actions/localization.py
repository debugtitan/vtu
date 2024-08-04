from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from billbuddy.utils import cfg, helpers, enums


async def localization_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard_template: list = cfg("start.toml").get("KEYBOARDS")["en"]
    await update.message.reply_text(
        f"{enums.ReactionType.INFO.value} please choose your preferred language",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
            helpers.create_inline_button(
                buttons=keyboard_template, callback_text="localization#"
            )
        ),
    )
