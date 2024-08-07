from telegram import Update
from telegram.ext import ContextTypes
from billbuddy.actions.menu import main_menu_handler
from billbuddy.utils import enums, decorators
from billbuddy.resources import dao


@decorators.is_valid_response
async def language_handler(
    update: Update, callback: ContextTypes.DEFAULT_TYPE, *args, **kwargs
):
    """handles the localization changes"""
    query = update.callback_query
    user = query.from_user
    lang_code = query.data.split("#")[1]
    await dao.setup_user_language(user.id, lang_code)
    await query.delete_message()
    return await main_menu_handler(update, callback)
