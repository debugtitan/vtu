from telegram import Update
from telegram.ext import ContextTypes

from billbuddy.utils import cfg, decorators
from billbuddy.resources.dao import get_user


@decorators.is_valid_response
async def balance_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
):
    lang = kwargs.get("lang", "en")
    msg_temp: str = cfg("balance.toml").get("BAL")[lang]
    user = await get_user(kwargs.get("id"))
    msg = msg_temp.format(user.balance, user.buddy_points)
    await update.message.reply_text(msg)
