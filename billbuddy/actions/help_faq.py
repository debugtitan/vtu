from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from billbuddy.utils import decorators, cfg


@decorators.is_valid_response
async def help_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
):
    lang = kwargs.get("lang", "en")
    msg_template: str = cfg("help.toml").get("HELP")[lang]
    await update.message.reply_text(msg_template, parse_mode=ParseMode.MARKDOWN)
