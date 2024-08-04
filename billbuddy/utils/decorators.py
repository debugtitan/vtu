import threading
from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatAction
from billbuddy.resources.dao.users import get_user
from billbuddy.utils import logger, cfg


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


def send_action(action):
    """Sends `action` while processing func command."""

    def send_action_helper(func):
        @wraps(func)
        async def command_func(
            update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
        ):
            await context.bot.send_chat_action(
                chat_id=update.effective_message.chat_id, action=action
            )
            return await func(update, context, *args, **kwargs)

        return command_func

    return send_action_helper


def private_chat_only(func):
    """Decorator to ensure that the command is only executed in a private chat."""

    @wraps(func)
    async def command_func(update: Update, context, *args, **kwargs):
        if update.effective_chat.type == "private":
            return await func(update, context, *args, **kwargs)

        logger.info(
            f"{update.message.from_user.id} {update.message.from_user.first_name}  called {update.message.text} from public chat"
        )

    return command_func


def user_restricted(func):
    """function that you want to restrict access to for certain users."""

    @wraps(func)
    async def command_func(
        update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
    ):
        try:
            user_id = update.message.from_user.id
        except AttributeError as err:
            user_id = update.callback_query.from_user.id
        user = await get_user(user_id)
        msg_template = cfg("bot.toml").get("BANNED")[user.language_code]
        if user.is_restricted:
            return await context.bot.send_message(user_id, msg_template)
        return await func(update, context, *args, **kwargs)

    return command_func


def is_valid_response(func):
    @wraps(func)
    @private_chat_only
    @user_restricted
    @send_action(ChatAction.TYPING)
    async def wrapper(update, callback, *args, **kwargs):
        await func(update, callback, *args, **kwargs)

    return wrapper
