import threading
from functools import wraps
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ChatAction
from billbuddy.utils import logger

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

def is_valid_response(func):
    @wraps(func)
    @private_chat_only
    @send_action(ChatAction.TYPING)
    async def wrapper(update, callback, *args, **kwargs):
        await func(update, callback, *args, **kwargs)

    return wrapper
